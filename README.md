# Good Deeds API
## Server part of the system aimed at connecting quarantined elderly with volunteers  

![alt text](resources/showcase.png?raw=True)  "Good Deed App")

### Problem  
Self-isolating, digitally excluded elderly:  
* Put themselves at risk of losing their lives every time they leave their house during the COVID-19 pandemic   
* They are not proficient in modern mobile technology  

Good-hearted people don’t know where, when and who needs help:  
* Nowadays people don’t know their neighbours as well as they used to in the past    

### The Solution  
Good Deeds is a system that connects two parties:  
* It uses a familiar voicemail system for elderly to leave a message asking for help   
* It provides a mobile app with a map that displays all active tasks in a local area for volunteers to pick up    


### Server Side 
An elderly person calls a number. The voicemail gets saved in the Zendesk customer suppor system.  
The server downloads all active voicemail tickets and corresponding mp3 files with voicemails.  
The mp3 files are converted into text using Google Speech-to-Text API.  
Postcodes are then turned into geographical coordinates. The server makes this data available in an API.

### Good Deeds API
The API is hosted on Heroku and can be accessed here:     
http://good-deeds-server.herokuapp.com/     
In order to download the data including longitude and latitude of the recorded voicemails, use:     
GET 'api/v1/resources/tickets/all'     
Or click  here to view all active voicemails:     
http://good-deeds-server.herokuapp.com/api/v1/resources/tickets/all     

Please note that the API can be disabled to reduce the costs of running it (due to using Google Cloud credits).  