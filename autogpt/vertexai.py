import google.generativeai as genai
"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

class Client:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)

    def completion(self, model: str, messages: list, temperature: float, max_tokens: int):
        generation_config = {
            "temperature": temperature,
            "top_p": 1,
            "top_k": 32,
            "max_output_tokens": max_tokens,
        }

        model = genai.GenerativeModel(model_name=model,
                              generation_config=generation_config,
                              safety_settings=self.safety_settings)
        print(messages)

        response = model.generate_content(messages)

        return response

    @property
    def safety_settings(self):
        return [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]
