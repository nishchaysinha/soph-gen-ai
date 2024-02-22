import google.generativeai as genai

class GenerativeModel:
    def __init__(self, model_name, api_key=None):
        if api_key is not None:

            genai.configure(api_key=api_key)
            generation_config = {
            "temperature": 0.25,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
            }
            self.model = genai.GenerativeModel(model_name)
        else:
            print("API key not found. Please set the GOOGLE_API_KEY environment variable.")
    
    def chat_object(self, history=[]):
        return self.model.start_chat(history=history)

