import logging
import requests
from utils.parser import extract_content

logging.basicConfig(level=logging.INFO)


class Groq:
    def __init__(self, token: str):
        self.token = token
        self.url = "https://api.groq.com/v1/request_manager/text_completion"
        self.logger = logging.getLogger(__name__)

    def complete(
        self,
        user_prompt: str,
        # history: list,
        model="mixtral-8x7b-32768",
        system_prompt="Please try to provide useful, helpful and actionable answers.",
        seed=10,
        max_tokens=32768,
        temperature=0.2,
        top_k=40,
        top_p=0.8,
        max_input_tokens=21845,
    ):
        payload = {
            "model_id": model,
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            # "history": history,
            "seed": seed,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_k": top_k,
            "top_p": top_p,
            "max_input_tokens": max_input_tokens,
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Accept": "*/*",
            "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=utf-8",
            "Referer": "https://groq.com/",
            "Origin": "https://groq.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-GPC": "1",
            "authorization": f"Bearer {self.token}",
            "Connection": "keep-alive",
            "TE": "trailers",
        }

        response = requests.post(self.url, headers=headers, json=payload)
        sentence = extract_content(response.text)
        return sentence
