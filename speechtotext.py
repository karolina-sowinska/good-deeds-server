from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import os


def transcribe_audio_to_text(local_file_path):
    """
    Transcribe a short audio file using Google synchronous speech recognition

    """
    client = speech_v1.SpeechClient()

    # The language of the supplied audio
    language_code = "en-US"

    # Sample rate in Hertz of the audio data sent
    # sample_rate_hertz = 9400


    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    config = {
        "language_code": language_code,
   
        "encoding": encoding,
    }

    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)

    for result in response.results:
            for alternative in result.alternatives:
                    f = open('flacs-transcribed/'+local_file_path[6:-4] + 'txt', 'a')
                    f.write("Transcript : "+ alternative.transcript + " \n" )

    return

         
def convert_mp3_to_flac():
    """
    Convert the mp3 files into the required FLAC fomat using AudioConvert library in bash script 
    """
    os.system('sh audioconvert.sh')


if __name__ == "__main__":
    
    convert_mp3_to_flac()
    
    for filename in os.listdir('flacs'):
        transcribe_audio_to_text("flacs/" + filename)

