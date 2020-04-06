import requests
from typing import List
import credentials

USR = credentials.USER
PWD = credentials.PWD

ZENDESK_URL = 'https://hackyeah.zendesk.com/api/v2/ticket_audits.json'

def query_zendesk_data(user: str, pwd: str) ->  List[dict]:
    """
    Queries the Zendesk API to download all active tickets (voicemails). 
    Retrieves ticket id, phone number, mp3_url, date of creation.
    Return a list of voicemail dicitionaries. 
    """

    # Do the HTTP get request
    response = requests.get(ZENDESK_URL, auth=(user, pwd))

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()

    tickets_data = []

    for ticket in data['audits']:
        if ticket['events'][0]['type'] == 'VoiceComment':
            single_ticket_data = {}
            
            ticket_id = ticket['events'][0]['id']
            phone = ticket['events'][0]['data']['from']
            mp3_url = ticket['events'][0]['data']['recording_url']
            created_at = ticket['events'][0]['data']['started_at']
            
            single_ticket_data['id'] = ticket_id
            single_ticket_data['mp3_url'] = mp3_url
            single_ticket_data['phone_number'] = phone
            single_ticket_data['created_at'] = created_at
            
            tickets_data.append(single_ticket_data)
            
    return tickets_data



def download_mp3s(tickets_data: List):
    """
    Downloads the mp3 files based on voicemail's mp3_urls 
    """

    for ticket in tickets_data:
        mp3_url = ticket['mp3_url']
        file_name = 'mp3/voicemail' + str(ticket['id']) +'.mp3'

        r = requests.get(mp3_url, auth=(USR, PWD))  
        f = open(file_name, 'wb')
        f.write(r.content)

    return

   