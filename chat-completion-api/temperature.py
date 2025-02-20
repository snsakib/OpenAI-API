from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt="""Summarize the following text into two concise bullet points:
Investment refers to the act of committing money or capital to an enterprise with the expectation of obtaining an added income or profit in return. There are a variety of investment options available, including stocks, bonds, mutual funds, real estate, precious metals, and currencies. Making an investment decision requires careful analysis, assessment of risk, and evaluation of potential rewards. Good investments have the ability to produce high returns over the long term while minimizing risk. Diversification of investment portfolios reduces risk exposure. Investment can be a valuable tool for building wealth, generating income, and achieving financial security. It is important to be diligent and informed when investing to avoid losses."""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_tokens=400,
  temperature=0
)

# Full response
print(response)

# Main response message
print(response.choices[0].message.content)

# Response Structure
ChatCompletion(
    id='chatcmpl-B2VWOG01fku9Uhd5MJ8vzW4XdlXYP',
    choices=[
        Choice(
            finish_reason='stop',
            index=0,
            logprobs=None,
            message=ChatCompletionMessage(
                content='ChatGPT was developed by OpenAI, an artificial intelligence research organization. OpenAI focuses on creating and promoting friendly AI for the benefit of humanity.',
                refusal=None,
                role='assistant',
                audio=None,
                function_call=None,
                tool_calls=None)
        )
    ],
    created=1739937524,
    model='gpt-4o-mini-2024-07-18',
    object='chat.completion',
    service_tier='default',
    system_fingerprint='fp_00428b782a',
    usage=CompletionUsage(
        completion_tokens=30,
        prompt_tokens=12,
        total_tokens=42,
        completion_tokens_details=CompletionTokensDetails(
            accepted_prediction_tokens=0,
            audio_tokens=0,
            reasoning_tokens=0,
            rejected_prediction_tokens=0
        ),
        prompt_tokens_details=PromptTokensDetails(
            audio_tokens=0,
            cached_tokens=0
        )
    )
)

