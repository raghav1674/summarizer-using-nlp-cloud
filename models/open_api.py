import os
import requests
import json
import re

# openapi chatgpt settings for text summary
OPEN_API_COMPLETION_ENDPOINT = "https://api.openai.com/v1/completions"
OPEN_API_BEARER_TOKEN = os.getenv('OPEN_API_BEARER_TOKEN') 
OPEN_API_MODEL = os.getenv("OPEN_API_MODEL")
OPEN_API_SUMMARIZE_KEYWORDS = "Summarize this for a second-grade student:  "

def get_summarized_text(text):
    url = OPEN_API_COMPLETION_ENDPOINT
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPEN_API_BEARER_TOKEN}'
    }
    text_without_whitespaces = re.sub('\s+',' ',text)

    payload=json.dumps({
        "model": OPEN_API_MODEL,
        "prompt": OPEN_API_SUMMARIZE_KEYWORDS +text_without_whitespaces,
        "temperature": 0.7,
        "max_tokens": 1000,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    })
    summary = "" 
    response = requests.post(url,data=payload,headers=headers)

    if response.ok:
        print(response.json())
        choices = response.json().get('choices')
        if len(choices):
            summary = choices[0]['text']
    else:
        raise Exception(response.json()['error']['message'])
    return summary.strip()
