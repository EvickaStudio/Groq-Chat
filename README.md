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

# Hello! Hello there, it's nice to meet you. I'm here to help answer any questions you have to the best of my ability. Do you have a specific question about a particular topic you'd like me to answer? I'm here to help, so let me know how I can assist you today.



# Stream response example
from text_completion.completion_stream import Groq as gqst

# Get Token
token = Token().get_token()

# Initialize Groq with token
groq = gqst(token)

response = groq.complete("What is the capital of France?")

# The capital of France is Paris. If you're interested in learning more about Paris, here are some actionable steps you can take:

# 1. Research Paris's rich history: Paris has a long and fascinating history that has played a significant role in shaping Western civilization. You can start by reading books or articles about Paris's history, or visiting websites dedicated to the city's past.
# 2. Plan a trip to Paris: If you have the opportunity, consider visiting Paris and experiencing its culture and history firsthand. There are many travel guides and websites that can help you plan your trip, including information on flights, accommodations, and attractions.
# 3. Learn French: While many people in Paris speak English, learning some basic French can enhance your experience and show respect for the local culture. There are many resources available for learning French, including language courses, apps, and online resources.
# 4. Explore French culture and cuisine: Paris is known for its culinary traditions, including croissants, baguettes, and escargot. You can try making some French dishes at home, or visit a French restaurant in your area to sample the cuisine.
# 5. Connect with French communities: There may be French communities in your area that you can connect with to learn more about the culture and practice your language skills. Consider joining a French club or group, or attending French cultural events in your community.
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
