from flask import Flask, request, jsonify
from flask_cors import CORS
from threading import Thread
from main import create_transcripts_new, playlist_dealer
from podcast import podcast_way

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
    try: 
        gpt = post_data.get('GPT', 'No gpt provided')
        print(gpt)
    except:
        return 404
    try: 
        source = post_data.get('source', 'No source provided')
        print(source)
    except:
        return 404
    if source == 1 :
        try:
            title = post_data.get('title', 'No title provided')
            print(title)
            link = post_data.get('link', 'no link provided')
            print(link)
            print("hello I am here")
            return_string = podcast_way(link, title, gpt)
            print("made here")
            post_data["Return String"] = return_string
        except:
            return 404
    else: 
        if typed==1:
            try:
                link = post_data.get('link', 'no link provided')
                print(link)
                return_string = create_transcripts_new(link, gpt)
                post_data["Return String"] = return_string
            except:
                return 404
        else: 
            post_data["Links"] = playlist_dealer(link, gpt)
        #create_transcripts(typed,0)
        #create_word_documents() 
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