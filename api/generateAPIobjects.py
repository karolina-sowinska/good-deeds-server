import os
import re 
from typing import List

from zendeskapi import query_zendesk_data
from credentials import USER, PWD

# This very neat regex is provided by UK Government to match British postcodes 
# A similiar solution can be easily created for any country
UK_REGEX = r"^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) {0,1}[0-9][A-Za-z]{2})"


def get_postcode(voicemail_content: str) -> str:

    matches = re.findall(UK_REGEX, voicemail_content.upper())
    #Unpack the result from a list and return the first element, which is the full match
    return matches[0][1]


def get_tickets_with_postcodes(tickets_data : List[dict]) -> List[dict]:
    tickets_data_with_postcodes = []

    for voicemail in os.listdir('flacs-transcribed') :

        f = open('flacs-transcribed/'+ voicemail, 'r')
        voicemail_content = f.read()

        voicemail_postcode = get_postcode(voicemail_content)
        voicemail_id = voicemail[9:-4]

        for ticket in tickets_data:
            if(ticket["id"] == int(voicemail_id)):
                ticket["postcode"] = voicemail_postcode
                tickets_data_with_postcodes.append(ticket)

    return tickets_data_with_postcodes

    
def get_coordinates_from_postcodes(tickets_data_with_postcodes : List[dict]) -> List[dict]:

    

    return 

                





    