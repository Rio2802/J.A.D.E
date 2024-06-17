from config import key
import requests
from mic_to_test1 import mic1

def chat1(chat):
    system_message = "I'm an AI assistant known as JADE, here to assist you."
    message_text = system_message + " " + chat
    message = {"role": "user", "parts": [{"text": message_text}]}
    data = {"contents": [message]}
    api_key = "AIzaSyDVTKI80bMig6faJ_10zfgQEzFRixJ5V5g"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    response = requests.post(url, json=data)

    if response.status_code == 200:
        t1 = response.json()
        candidates = t1.get("candidates")
        if candidates:
            content = candidates[0].get("content")
            if content:
                parts = content.get("parts")
                if parts:
                    generated_text = parts[0].get("text")
                    print("Generated Text:", generated_text)
                else:
                    print("Error: No 'parts' in content")
            else:
                print("Error: No 'content' in candidates")
        else:
            print("Error: No candidates in response")
    else:
        print("Error:", response.status_code, response.text)

chat = mic1()
chat1(chat)
