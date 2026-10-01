from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_failure(error_message):

    prompt = f"""
    Analyze this Playwright automation failure.

    Error:
    {error_message}

    Provide:
    1. Possible root cause
    2. Recommended fix
    3. Whether it looks like a locator,
       synchronization, application, or environment issue.
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text