import os
import requests

# meaning cloud creds for text summary
MEANING_CLOUD_SUMMARIZE_ENDPOINT = "https://api.meaningcloud.com/summarization-1.0"
MEANING_CLOUD_API_KEY = os.getenv('MEANING_CLOUD_API_KEY')

def get_summarized_text(text):
    url = MEANING_CLOUD_SUMMARIZE_ENDPOINT

    payload={
        'key': MEANING_CLOUD_API_KEY ,
        'txt': text,
        'limit': 70
    }
    return requests.post(url,data=payload).json()['summary']