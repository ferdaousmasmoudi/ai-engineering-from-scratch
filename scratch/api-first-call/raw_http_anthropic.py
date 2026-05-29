import os
import json
import urllib.request
import urllib.error
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY is missing. Add it to your .env file.")

url = "https://api.anthropic.com/v1/messages"

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01",
}

body = {
    "model": "claude-sonnet-4-6",
    "max_tokens": 256,
    "messages": [
        {
            "role": "user",
            "content": "What is a neural network in one sentence?"
        }
    ],
}

data = json.dumps(body).encode("utf-8")

request = urllib.request.Request(
    url=url,
    data=data,
    headers=headers,
    method="POST",
)

try:
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        result = json.loads(response_body)

        print(result["content"][0]["text"])

except urllib.error.HTTPError as error:
    print("HTTP error:", error.code)
    print(error.read().decode("utf-8"))

except urllib.error.URLError as error:
    print("URL/network error:", error.reason)
