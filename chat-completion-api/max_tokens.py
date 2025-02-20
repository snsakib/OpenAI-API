from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt = """Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. 
It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. 
Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, 
such as commuting, travel, and transportation of goods. 
Cars are often associated with freedom, independence, and mobility.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": prompt
    }],
    max_tokens=100
)

# Full response
print(response)

# Main response message
print(response.choices[0].message.content)

# Response Structure
# ChatCompletion(
#     id='chatcmpl-B2VWOG01fku9Uhd5MJ8vzW4XdlXYP',
#     choices=[
#         Choice(
#             finish_reason='stop',
#             index=0,
#             logprobs=None,
#             message=ChatCompletionMessage(
#                 content='ChatGPT was developed by OpenAI, an artificial intelligence research organization. OpenAI focuses on creating and promoting friendly AI for the benefit of humanity.',
#                 refusal=None,
#                 role='assistant',
#                 audio=None,
#                 function_call=None,
#                 tool_calls=None)
#         )
#     ],
#     created=1739937524,
#     model='gpt-4o-mini-2024-07-18',
#     object='chat.completion',
#     service_tier='default',
#     system_fingerprint='fp_00428b782a',
#     usage=CompletionUsage(
#         completion_tokens=30,
#         prompt_tokens=12,
#         total_tokens=42,
#         completion_tokens_details=CompletionTokensDetails(
#             accepted_prediction_tokens=0,
#             audio_tokens=0,
#             reasoning_tokens=0,
#             rejected_prediction_tokens=0
#         ),
#         prompt_tokens_details=PromptTokensDetails(
#             audio_tokens=0,
#             cached_tokens=0
#         )
#     )
# )

