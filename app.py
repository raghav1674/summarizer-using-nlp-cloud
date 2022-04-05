import os
from flask import Flask,request,jsonify

from utils import get_summarized_text, read_from_document, read_from_url, read_from_video
from health_dummy_text import text


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, This is an backend for summarizing text"

@app.route('/health')
def health():
    return jsonify({"summary_text" : get_summarized_text(text)})

@app.route('/summarize/<string:data_key>',methods=['POST'])
def summarize(data_key):
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
            text = read_from_video(data_value)
    if text:
        response = get_summarized_text(text)
    else:
        response = 'Hello , Please provide valid input'
    return jsonify({"summary_text" : response})



if __name__ == '__main__':
    port = os.getenv('PORT') or 4000
    app.run(host='0.0.0.0',port=port)




