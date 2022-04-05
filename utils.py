import os
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import nlpcloud

NLP_CLOUD_MODEL = os.getenv('NLP_CLOUD_MODEL') 
NLP_CLOUD_TOKEN = os.getenv('NLP_CLOUD_TOKEN') 

nlp_cloud_client = nlpcloud.Client(NLP_CLOUD_MODEL,NLP_CLOUD_TOKEN)

def read_from_video(video_id):
    response_data = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = ''
    for each_text in response_data:
        full_text += ' '+ each_text['text']
    return full_text

def read_from_url(url):

    full_text = requests.get(url)
    return full_text.text

def read_from_document(file):
    return file.read().decode()

def get_summarized_text(text):
    response  = nlp_cloud_client.summarization(text)
    return response['summary_text']
    
