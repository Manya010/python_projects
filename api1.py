import requests
import pyautogui as pg
import time
import random

def get_random_animal_photo():
    # Unsplash API endpoint for random cute animal photos
    url = "https://api.unsplash.com/photos/random"
    params = {
        "query": "cute animals",
        "client_id": "t5179SOC-HMLeHt3KlIIAy1vjv1jUkE_3_iN3gB7PBM"  # Replace with your Unsplash API access key
    }
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code == 200:
        # Extract the photo URL
        photo_url = data["urls"]["regular"]
        return photo_url
    else:
        print("Failed to fetch photo:", data["errors"])
        return None

def send_message_with_photo(message):
    photo_url = get_random_animal_photo()
    if photo_url:
        # Wait for 8 seconds for you to navigate to the WhatsApp chat
        time.sleep(8)
        
        # Send the message with the photo
        pg.write(message)
        pg.press("enter")
        time.sleep(1)  # Small delay to avoid detection as spam
        pg.write(photo_url)
        pg.press("enter")

if __name__ == "__main__":
    cute_messages = [
        "Hey cutie! 🐾 Just wanted to brighten your day with some adorable furry friends! 💖",
        "Thinking of you! 🌸 Here's a little dose of cuteness to make you smile! 😊",
        "Hello love! 💕 Sending you lots of cuddles and cute animal pics! 🐻🐶🐱",
        "Hey sweetheart! 💞 Hope this makes your day a little brighter! 🌈"
    ]

    for _ in range(4):
        # Select a random cute message
        message = random.choice(cute_messages)
        send_message_with_photo(message)
        time.sleep(1)  # Add a delay between each message to avoid rate limits and spam detection























