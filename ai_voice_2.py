import boto3
import io
import pygame  

def speak_text(text: str):
    """Speak the given text using Amazon Polly and play it directly."""
    polly_client = boto3.client('polly', 
                                region_name='us-east-1',  
                                aws_access_key_id='YOUR_AWS_ACCESS_KEY', 
                                aws_secret_access_key='YOUR_AWS_SECRET_KEY')

    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'  
    )

    audio_stream = response['AudioStream'].read()

    pygame.mixer.init()

    sound = pygame.mixer.Sound(io.BytesIO(audio_stream))

    sound.play()

    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)  

# speak_text("Hello, how are you?")

