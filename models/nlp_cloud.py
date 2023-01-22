import os
import nlpcloud

# nlp cloud creds for text summary
NLP_CLOUD_MODEL = os.getenv('NLP_CLOUD_MODEL') 
NLP_CLOUD_TOKEN = os.getenv('NLP_CLOUD_TOKEN') 

nlp_cloud_client = nlpcloud.Client(NLP_CLOUD_MODEL,NLP_CLOUD_TOKEN)

def get_summarized_text(text):
    response  = nlp_cloud_client.summarization(text)
    return response['summary_text']
