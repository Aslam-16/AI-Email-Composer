
from openai import OpenAI
from google import genai
from google.genai import types

def generate_response(model, api_key,session_state,system_prompt=None,gemini_session_state=None):
    response_content=None
    try:
        if model=="ChatGpt":
                client=OpenAI(api_key=api_key)
                response=client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=session_state
                )
                response_content=response.choices[0].message.content
        else:
                client=genai.Client(api_key=api_key)
                response=client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=gemini_session_state,
                    config=types.GenerateContentConfig(
                    system_instruction=system_prompt
        )
                )
                response_content=response.text
        return response_content
    except Exception as e:
          raise Exception(f"Error generating response: {str(e)}")