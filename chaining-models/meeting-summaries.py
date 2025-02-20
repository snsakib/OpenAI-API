from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the datacamp-q2-roadmap.mp3 file
audio_file = open("datacamp-q2-roadmap.mp3", "rb")

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Create a request to the API to summarize the transcript into bullet points
chat_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Summarize the transcript into bullet points: " + audio_response.text}
    ],
    max_tokens=100
)
print(chat_response.choices[0].message.content)