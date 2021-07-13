# Made by Hxnter69
@Huñter 
# Made by Huñter#9934
import random
import requests
from discord_webhook import DiscordWebhook
import json
webhook_url = ''
user_string = input("Enter string to generate:")
user_value = 0
print("Enter the character length:")
# Checks if the integer is between Roblox's character limit
while True:
   try:
       while (user_value < 3) or (user_value > 20):
           user_value = int(input("Enter an integer between 3 and 20."))
       break
   except ValueError:
       print("Enter a valid integer.")
# Generates random list then converts into string
# Loop starts here

while True:
    try:
       char_list = list(user_string)
       char = random.choices(char_list, k=user_value)
       
       username = "".join(char)
       r = requests.get(f"https://auth.roblox.com/v1/usernames/validate?request.username={username}&request.birthday=1969%2F04%2F20&request.context=Signup")
       dic = json.loads(r.text)
       if int(dic["code"]) == 0:
           print(dic["message"]+": "+username)
           webhook = DiscordWebhook(url=webhook_url, content=f'New Username Found! {username}')
           response = webhook.execute()
           with open("usernames.txt", "a") as f:
               f.write(username + "\n")
       elif int(dic["code"]) != 0:
           print(dic["message"] + ": " +username)
    except:
        pass 
