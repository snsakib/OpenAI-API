from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Write an appropriate prompt to help the model
prompt = "The audio relates to a recent World Bank report"

# Create a translation from the audio file
response = client.audio.translations.create(model="whisper-1",
                                            file=audio_file,
                                            prompt=prompt)

print(response.text)

# Full Response Structure
# Translation(
#     text='Hello, my name is Eduardo, I am a CTO at Datacamp. I hope you are enjoying this course that James and I have created for you. This API allows you to send an audio and bring it to English. The original audio is in Portuguese.'
# )
