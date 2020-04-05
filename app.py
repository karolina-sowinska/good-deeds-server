import os
import flask
from flask import request, jsonify
from boto.s3.connection import S3Connection

from credentials import USER, PWD
from zendeskapi import query_zendesk_data, download_mp3s
from generateAPIobjects import get_tickets_with_postcodes, get_coordinates_from_postcodes
from speechtotext import transcribe_audio_to_text, convert_mp3_to_flac


s3 = S3Connection(os.environ['GOOGLE_APPLICATION_CREDENTIALS'], os.environ['GOOGLE_CREDENTIALS'])


app = flask.Flask(__name__)
app.config["DEBUG"] = True

#set the Google credentials key 

@app.route('/', methods=['GET'])
def home():
    return "<h1> GOOD DEEDS API </h1> <p> In order to download the data, use GET '/api/v1/resources/tickets/all </p>"

@app.route('/api/v1/resources/tickets/all', methods=['GET'])
def api_all():

    #Query Zendesk API
    tickets_data = query_zendesk_data(USER, PWD)

    #Download mp3s from ticket mp3 urls
    download_mp3s(tickets_data)

    #Convert mp3s into FLAC format
    convert_mp3_to_flac() 

    #Transcribe audio into text using Google Speech to Text API
    for filename in os.listdir('flacs'):
        transcribe_audio_to_text("flacs/" + filename)

    #Retrieve post codes from text and add them to the object
    tickets_data_with_postcodes = get_tickets_with_postcodes(tickets_data)

    #Retrieve geo coordinates from post codes and add them to objects
    tickets_data_with_coordinates = get_coordinates_from_postcodes(tickets_data_with_postcodes)

    #Jsonify and return the data 
    return jsonify(tickets_data_with_coordinates)


if __name__ == "__main__":
    app.debug = True
    app.run()