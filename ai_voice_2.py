import boto3
import io
import pygame  # To play the audio directly

def speak_text(text: str):
    """Speak the given text using Amazon Polly and play it directly."""
    # Create a Polly client with your AWS credentials and region specified
    polly_client = boto3.client('polly', 
                                region_name='us-east-1',  # Region of your choice
                                aws_access_key_id='YOUR_AWS_ACCESS_KEY', 
                                aws_secret_access_key='YOUR_AWS_SECRET_KEY')

    # Synthesize the speech
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'  # You can change the voice here (e.g., 'Joanna', 'Matthew', 'Ivy')
    )

    # Get the audio stream from the response
    audio_stream = response['AudioStream'].read()

    # Initialize pygame mixer to play the sound
    pygame.mixer.init()

    # Convert the audio stream to a pygame sound object
    sound = pygame.mixer.Sound(io.BytesIO(audio_stream))

    # Play the sound
    sound.play()

    # Wait until the sound has finished playing
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)  # Check every 10ms

# Example usage
speak_text("Hello, how are you?")
