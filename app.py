# core
import os
from flask import Flask,request,jsonify

# utils
from utils import read_from_document, read_from_url, read_from_video
from health_dummy_text import text

# models
import models.meaning_cloud as meaning_cloud
import models.open_api as open_api
import models.nlp_cloud as nlp_cloud

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, This is an backend for summarizing text"

@app.route('/health')
def health():
    return jsonify(
        {
            # "summary_text_from_nlp_cloud" : nlp_cloud.get_summarized_text(text),
            # "summary_text_from_meaning_api" : meaning_cloud.get_summarized_text(text),
            "summary_text_from_open_api" : open_api.get_summarized_text(text),
        }
    )

@app.route('/summarize/<string:data_key>',methods=['POST'])
def summarize(data_key):
    try:
        text = None
        if data_key == 'file':
            file_store = request.files['src_file']
            text = read_from_document(file_store)
        else:
            data = request.get_json()
            data_value = data[data_key]
            text = data_value 
            if data_key == 'url':
                text = read_from_url(data_value)
            elif data_key == 'video':
                video_id = data_value.split('/')[-1]
                text = read_from_video(video_id)
        if text:
        #     if data_key == 'text':
            response = open_api.get_summarized_text(text)
            # else:
            #     response = meaning_cloud.get_summarized_text(text)
        else:
            response = 'Hello , Please provide valid input'
        return jsonify({"summary_text" : response})
    except Exception as e:
        print(e)
        return jsonify({"summary_text" : 'Some error happened',"error": f'{e}'})


if __name__ == '__main__':
    port = os.getenv('PORT') or 5000
    app.run(host='0.0.0.0',port=port)




