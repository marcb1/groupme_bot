import os
from flask import Flask
from flask import request
import requests
import random
import codecs

#API id
#move this to a config file
bot_id = ''


app = Flask(__name__)

#encode string as ASCII
def stripped(text):
	text = text.lower()
	return text.encode('ascii','replace_spc')

def send(text):
	message = {
		'text' : text,
		'bot_id' : bot_id
	}
	r = requests.post("https://api.groupme.com/v3/bots/post", params = message)

@app.route('/', methods=['POST'])
def message():
	if not request.json or not 'text' in request.json:
		return
	
	user_id = request.json['user_id']
	nick = request.json['name'].lower()
	message = request.json['text'].lower()
	message = stripped(message).strip()

        print 'Got message' + message
        message_callback.got_message(message, nick);
        return ''

if __name__ == "__main__":
     app.run(port = 8080, host = '0.0.0.0', debug = True)
