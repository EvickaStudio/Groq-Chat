import requests
import json

# URL der API
url = "https://api.groq.com/v1/request_manager/text_completion"

# Zu sendende Daten
data = {
    "model_id": "mixtral-8x7b-32768",
    "system_prompt": "Please try to provide useful, helpful and actionable answers.",
    "user_prompt": "hiii",
    "history": [
        {
            "user_prompt": "Hello, can zou tell me something fun about germany",
            "assistant_response": "Hello! I'm here to help answer your questions and provide useful, helpful, and actionable information. Is there something specific you would like to know or discuss? I'm here to assist you to the best of my ability.",
        }
    ],
    "seed": 10,
    "max_tokens": 32768,
    "temperature": 0.2,
    "top_k": 40,
    "top_p": 0.8,
    "max_input_tokens": 21845,
}

# HTTP-Header
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImVkODA2ZjE4NDJiNTg4MDU0YjE4YjY2OWRkMWEwOWE0ZjM2N2FmYzQiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiI5NTIwNjQ0MjA1OTAtc2ZiOG81NGxlcWQwZGViczZyZmNycWJ1ZmU0M2U3c2suYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhenAiOiJhbm9ueW1vdXMtYXBpLXVzZXJAZ3JvcS1jbG91ZC1zdGFnaW5nLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwiZW1haWwiOiJhbm9ueW1vdXMtYXBpLXVzZXJAZ3JvcS1jbG91ZC1zdGFnaW5nLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV4cCI6MTcwNzc0Nzc2NywiaWF0IjoxNzA3NzQ0MTY3LCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJzdWIiOiIxMTY4MjY2OTYyNzQ1NzAzNTg4NTcifQ.h73RDfBxne0BrUlyiD9wCBYtRwias2leBqnvmBiILVYPXPmSsa70le2ys3T7LFVYTB1FD0OXiN7e9Dpiwhkrxui7hgALVEk9pjkyxJkwvcU_GjCnkAebzd39n0G5iqs-tdRoAGa5i_6ckr50BDij9Bl2286lg6chNhUvMbFra6qlfob13FfiyMkkAVWCROC8300rBCCU4WRYUPTnlUnx0_2XYKrw4sPYA_8KfoGHAruAyTletWtvIFwC-gHsL82gZm374lp43yYLsa7DiERzyXkq0-o-a7kvC9AW2lCk2xmMT94zx1bq-AJeVzSDmrWLkfdvXzdBePOAiwTr__aMgg",  # Ersetzen Sie <Ihr Token hier> mit Ihrem tatsächlichen Bearer Token
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "*/*",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://groq.com/",
    "Origin": "https://groq.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1",
}

try:
    with requests.post(
        url, headers=headers, json=data, stream=True, timeout=30, verify=True
    ) as response:
        response.raise_for_status()  # Überprüft auf HTTP-Fehler
        buffer = ""
        for chunk in response.iter_content(
            chunk_size=1024
        ):  # Verarbeitet die Antwort in Chunks von 1024 Bytes
            if chunk:  # Filtert Keep-Alive neue Chunks aus
                chunk_str = chunk.decode("utf-8")  # Decode bytes to string
                buffer += chunk_str
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    response_json = json.loads(line)  # Parse each line as JSON
                    if content := response_json.get("result", {}).get("content"):
                        print(content, end="")
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Oops: Something Else", err)
except json.JSONDecodeError as json_err:
    print("JSON Decode Error:", json_err)
