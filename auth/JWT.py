import requests
from typing import Optional
import logging


class Token:
    """
    Class to get a JWT token from the Groq API.

    The token is only valid for 1 hour.
    """

    def __init__(self):
        self.url = "https://api.groq.com/v1/auth/anon_token"
        self.logger = logging.getLogger(__name__)

    def get_token(self) -> Optional[str]:
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.json()["access_token"]
            else:
                self.logger.error(
                    f"Failed to get token. Status code: {response.status_code}"
                )
                return None
        except Exception as e:
            self.logger.error(f"An error occurred while getting the token: {e}")
            return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    jwt = Token()
    token = jwt.get_token()
    if token:
        print(token)
    else:
        print("Failed to get token.")
