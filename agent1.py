import requests
import task1  # Assuming task1 contains the definitions of functions

def parse_function_response(message):
    function_call = message[0].get("functionCall")
    function_name = function_call["name"]
    print("Gemini: call function", function_name)
    try:
        arguments = function_call.get("args")
        print("Gemini: arguments are", arguments)
        if arguments:
            d = getattr(task1, function_name)
            print("function is", d)
            function_response = d(**arguments)
        else:
            function_response = "No Arguments"
    except Exception as e:
        print(e)
        function_response = "Invalid response"
    return function_response

def run_conversation(user_message):
    system_message = """You are an AI bot that can do everything using function calls. When you are asked to do something using a function call, you have available and then respond with a message."""  # first Ins
    message_text = system_message + "\n" + user_message
    message = {"role": "user", 
               "parts": [{"text": message_text}]}  
    messages = [message]  # Initialize messages list
    
    data = {"contents": messages,
            "tools": [{"functionDeclarations": task1.definitions
                 }]
            }
    api_key = "AIzaSyDVTKI80bMig6faJ_10zfgQEzFRixJ5V5g"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    response = requests.post(url, json=data)

    if response.status_code != 200:
        print(response.text)

    t1 = response.json()
    if "candidates" not in t1 or not t1.get("candidates"):
        print("Error: No response generated")
        return None
    
    message = t1.get("candidates")[0].get("content").get("parts")
    if message and 'functionCall' in message[0]:
        resp1 = parse_function_response(message)
        return resp1

if __name__ == "__main__":
    user_message = "Find the IP address of google.com"
    print(run_conversation(user_message))
