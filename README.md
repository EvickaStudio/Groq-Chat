# GROQ Chat

A very simple wrapper for the GROQ chat completion API. The response time is quite fast, faster than other alternatives I have tried.

> [!NOTE]
> This is not the best way to implement this, it took around 20/30 minutes to get this working, but it works. Altough, I have not tested this with a large amount of data.

## Project Structure

The project is organized as follows:

- `auth/`: Contains the JWT authentication logic.
- `text_completion/`: Contains the text completion logic.
- `utils/`: Contains a simple parser for the stream response.
- `main.py`: The main entry point of the application.

## Setup

1. Clone the repository:

```sh
git clone https://github.com/EvickaStudio/Groq-Chat.git
```

2. Navigate to the project directory:

```sh
cd Groq-Chat
```

## Usage

Install the dependencies:

```sh
pip install -r requirements.txt
```

Run the main script after editing:

```sh
python main.py
```

## Implementation

```python
# Import modules:

from auth.JWT import Token
from text_completion.completion import Groq

# Get an token, if you don't have one.
token = Token().get_token()

# Create an instance of the Groq class with the token.
chat = Groq(token)

# Get the completion for the text "Hello world!".
response = chat.complete("Hello world!")

# Print the response.
print(response)



# Stream response example
from text_completion.completion_stream import Groq as gqst

# Get Token
token = Token().get_token()

# Initialize Groq with token
groq = gqst(token)

response = groq.complete("What is the capital of France?")

```

## Info

The `JWT.py` gets an "anonymous" token from the API. The token is only valid for an hour.

Here is an example token information:

```json
{
  "aud": "952064420590-sfb8o54leqd0debs6rfcrqbufe43e7sk.apps.googleusercontent.com",
  "azp": "anonymous-api-user@groq-cloud-staging.iam.gserviceaccount.com",
  "email": "anonymous-api-user@groq-cloud-staging.iam.gserviceaccount.com",
  "email_verified": true,
  "exp": 1707744173, // 3600 seconds = 1 hour
  "iat": 1707740573,
  "iss": "https://accounts.google.com",
  "sub": "116826696274570358857"
}
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
