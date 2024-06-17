import requests
import socket

def get_ip(host):
    try:
        result = socket.getaddrinfo(host, None)
        ip_addresses = [addr[4][0] for addr in result]
        return ip_addresses
    except Exception as e:
        print(e)
        return f"Error in finding the IP: {e}"

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"
    querystring = {
        "location": city,
        "format": "json",
        "u": "f"
    }
    headers = {
        "X-RapidAPI-Key": "db49b0079amshec40358b0ec4568p1c9f55jsn0a3fee6c5c38",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com" 
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise error for bad response status
        data = response.json()  # Parse JSON response

        location = data.get("location")
        if location:
            print(f"Weather information for {location.get('city')}, {location.get('country')}:")

        current_observation = data.get("current_observation")
        if current_observation:
            temperature = current_observation.get("condition", {}).get("temperature")
            condition = current_observation.get("condition", {}).get("text")
            print(f"The current temperature is {temperature}°F with {condition}.")

            atmosphere = current_observation.get("atmosphere")
            if atmosphere:
                humidity = atmosphere.get("humidity")
                print(f"The humidity is {humidity}%.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

definitions = [
    {
        "name": "temp_city",
        "description": "Find the Weather, Temperature of a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City to find the weather"
                }
            }
        }
    },
    {
        "name": "temp_room",
        "description": "Find the Temperature of my room or my home",
        "parameters": {
            "type": "object",
            "properties": {
                "room": {
                    "type": "string",
                    "description": "room or home"
                }
            }
        }
    },
    {
        "name": "get_ip",
        "description": "Find the IP address",
        "parameters": {
            "type": "object",
            "properties": {
                "host": {
                    "type": "string",
                    "description": "URL to get the IP address"
                }
            }
        }
    }
]

if __name__ == "__main__":
    temp_city("Mumbai")
