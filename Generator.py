# Made by Hxnter69
import random
import requests
import time
import tasks
from discord_webhook import DiscordWebhook, DiscordEmbed
import keep_alive
import json
keep_alive.keep_alive()
webhook_url = 'WEBHOOK_URL_HERE'
user_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'
user_value = 5

while True:
    try:
       char_list = list(user_string)
       char = random.choices(char_list, k=user_value)
       
       username = "".join(char)
       r = requests.get(f"https://auth.roblox.com/v1/usernames/validate?request.username={username}&request.birthday=1969%2F04%2F20&request.context=Signup")
       dic = json.loads(r.text)
       if int(dic["code"]) == 0:
           print(dic["message"]+": " +username)
           
           time.sleep(1.50)
           
           webhook = DiscordWebhook(url=webhook_url)
           
           embed = DiscordEmbed(title='Username Generator', description=f'{username}', color='ff2050')
           
           webhook.add_embed(embed)
          
           response = webhook.execute()
           with open("usernames.txt", "a") as f:
               f.write(username + "\n")
       elif int(dic["code"]) != 0:
           print(dic["message"] + ": " +username)
    except:
        pass
