from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the audio.wav file
audio_file = open('audio.wav', "rb")

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Create a request to the API to identify the language spoken
chat_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= [
        {"role": "user", "content": "What is language of the following text: " + audio_response.text}
    ]
)
print(chat_response.choices[0].message.content)