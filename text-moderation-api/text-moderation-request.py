from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Moderation endpoint
response = client.moderations.create(
    model="text-moderation-latest",
    input="My favorite book is To Kill a Mockingbird."
)

print(response)

# Full Response Structure
# ModerationCreateResponse(
#     id='modr-B31gsfyoOcNhC9UXgcqwT60mcljz7',
#     model='text-moderation-007',
#     results=[
#         Moderation(
#             categories=Categories(
#                 harassment=False,
#                 harassment_threatening=False,
#                 hate=False,
#                 hate_threatening=False,
#                 illicit=None,
#                 illicit_violent=None,
#                 self_harm=False,
#                 self_harm_instructions=False,
#                 self_harm_intent=False,
#                 sexual=False,
#                 sexual_minors=False,
#                 violence=False,
#                 violence_graphic=False,
#                 self-harm=False,
#                 sexual/minors=False,
#                 hate/threatening=False,
#                 violence/graphic=False,
#                 self-harm/intent=False,
#                 self-harm/instructions=False,
#                 harassment/threatening=False
#             ),
#             category_applied_input_types=None,
#             category_scores=CategoryScores(
#                 harassment=5.243551186140394e-06,
#                 harassment_threatening=1.1516095810293336e-06,
#                 hate=4.767837526742369e-05,
#                 hate_threatening=3.2021056028952444e-08,
#                 illicit=None,
#                 illicit_violent=None,
#                 self_harm=9.466615438213921e-07,
#                 self_harm_instructions=5.426785065765216e-08,
#                 self_harm_intent=1.5536235764557205e-07,
#                 sexual=3.545879735611379e-06,
#                 sexual_minors=1.1304399549771915e-06,
#                 violence=0.0001064608441083692,
#                 violence_graphic=1.086988686438417e-05,
#                 self-harm=9.466615438213921e-07,
#                 sexual/minors=1.1304399549771915e-06,
#                 hate/threatening=3.2021056028952444e-08,
#                 violence/graphic=1.086988686438417e-05,
#                 self-harm/intent=1.5536235764557205e-07,
#                 self-harm/instructions=5.426785065765216e-08,
#                 harassment/threatening=1.1516095810293336e-06
#             ),
#             flagged=False
#         )
#     ]
# )
