import os
import openai
import argparse
import re
from typing import List

MAX_INPUT_LENGTH = 48

def main():
  # Parse command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', '-i', type=str, required=True)
  args = parser.parse_args()
  user_input = args.input
  
  # Output the user input
  print(f'User input: {user_input}')
  if validate_length(user_input):
    generate_branding_snippet(user_input)
    generate_keywords(user_input)
  else:
    raise ValueError(
      f'Could not generate keywords and snippet from {user_input}. Please make sure your input is below {MAX_INPUT_LENGTH} characters'
    )
# Checks the length of the user input 
def validate_length(prompt: str):
  return len(prompt) <= MAX_INPUT_LENGTH
  
  
 
def generate_keywords(prompt: str):
  openai.api_key = os.getenv('OPENAI_API_KEY')
  openai.organization = 'org-bvCghBdftRDnvFLBdwm7n449'

  enriched_prompt = f'Generate related branding keywords for {prompt}: '
  print(enriched_prompt)
  response = openai.Completion.create(
    engine='text-davinci-001', prompt=enriched_prompt, max_tokens=48
  )
  keywords_text: str = response['choices'][0]['text']
  keywords_text = keywords_text.strip()
  keywords_array = re.split(', | \n | * | - | ;', keywords_text)
  keywords_array = [k.lower().strip() for k in keywords_array]
  keywords_array = [k for k in keywords_array if len(k) > 0]
  
  print(f'Keywords: {keywords_array}')
  
  return keywords_array


def generate_branding_snippet(prompt: str):

  openai.api_key = os.getenv('OPENAI_API_KEY')
  openai.organization = 'org-bvCghBdftRDnvFLBdwm7n449'

  enriched_prompt = f'Generate upbeat branding snippet for {prompt}: '
  print(enriched_prompt)
  
  response = openai.Completion.create(
    engine='text-davinci-001', prompt=enriched_prompt, max_tokens=48
  )
  branding_text: str = response['choices'][0]['text']
  branding_text = branding_text.strip()
  last_char = branding_text[-1]
  if last_char not in {'.', '!', '?'}:
    branding_text += '...'
  
  print(f'Snippet: {branding_text}')
  return branding_text

if __name__ == '__main__':
  main()