import json

def extract_content(response):
    decoder = json.JSONDecoder()
    sentence = ""
    while response:
        obj, idx = decoder.raw_decode(response)
        response = response[idx:].lstrip()
        if "content" in obj["result"]:
            sentence += obj["result"]["content"]
    return sentence
