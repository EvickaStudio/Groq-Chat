from auth.JWT import Token

# Normal mode
from text_completion.completion import Groq as gq

# Get Token
token = Token().get_token()
print(token)

# Initialize Groq with token
groq = gq(token)

response = groq.complete("What is the capital of France?")

print(response)



# Stream response example
from text_completion.completion_stream import Groq as gqst

# Get Token
token = Token().get_token()

# Initialize Groq with token
groq = gqst(token)

response = groq.complete("What is the capital of France?")
