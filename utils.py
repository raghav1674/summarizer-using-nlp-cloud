from youtube_transcript_api import YouTubeTranscriptApi
import requests

def read_from_video(video_id):
    try:
        response_data = YouTubeTranscriptApi.get_transcript(video_id,languages=['en','en-IN'])
        full_text = ''
        for each_text in response_data:
            full_text += ' '+ each_text['text']
        return full_text
    except Exception as e:
        raise Exception(f'{e}')

def read_from_url(url):

    full_text = requests.get(url)
    return full_text.text

def read_from_document(file):
    return file.read().decode()
