from auth.JWT import Token
from text_completion.completion import Groq

token = Token().get_token()
print(token)

groq = Groq(token)

response = groq.complete("What is the capital of France?")

print(response)
