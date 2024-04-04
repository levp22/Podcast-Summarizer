from flask import Flask, request, jsonify
from flask_cors import CORS
from threading import Thread
from main import create_transcripts_new

app = Flask(__name__)
CORS(app)
posts = []

@app.route('/posts', methods=['POST'])
def add_post():
    post_data = request.json
    try: 
        typed = post_data.get('type', 'No type provided')
        print(typed)
    except:
        return 404
    if typed==1:
        link = post_data.get('link', 'no link provided')
        print(link)
        return_string = create_transcripts_new(link)
    else: 
        return_string = " "
    #create_transcripts(typed,0)
    #create_word_documents() 
    post_data["Return String"] = return_string
    posts.append(post_data)
    print("hello")
    post = jsonify(post_data)
      
    return post, 201

from werkzeug.serving import run_simple

def run_app():
    run_simple('localhost', 5000, app)

# Then start the thread as before
flask_thread = Thread(target=run_app)
flask_thread.start()