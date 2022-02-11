from fastapi import FastAPI, HTTPException
from nakala import generate_keywords, generate_snippet, phrase_length

app = FastAPI()
MAX_PHRASE_LENGTH = 49


@app.get('/generate_snippet')
async def generate_snippet_api(prompt: str):
  validate_phrase_length(prompt)
  snippet = generate_snippet(prompt)
  return {'snippet': snippet, 'keywords': []}

@app.get('/generate_keywords')
async def generate_keywords_api(prompt: str):
  validate_phrase_length(prompt)
  keywords = generate_keywords(prompt)
  return {'snippet': None ,'keywords': keywords}

@app.get('/generate_caption')
async def generate_caption_api(prompt: str):
  validate_phrase_length(prompt)
  snippet = generate_snippet(prompt)
  keywords = generate_keywords(prompt)
  length = phrase_length(prompt)
  return {'length': length, 'snippet': snippet, 'keywords': keywords}

def validate_phrase_length(prompt: str):
  if len(prompt) >= MAX_PHRASE_LENGTH:
    raise HTTPException(
      status_code=400, 
      detail='Your have exceeded the maximum allowed limit of {MAX_INPUT_LENGTH} characters. Please try a shorter phrase.')
  pass


# uvicorn nakala_api:app --reload