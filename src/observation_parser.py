from openai import OpenAI

client = OpenAI()

def extract_observations(text):

    prompt = f"""
    Extract structured observations from the following inspection text.

    Return in JSON format with fields:
    - area
    - observation
    - thermal_finding
    - possible_issue

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content