# Made by Hxnter69
import random
import requests
import time
import string
from discord_webhook import DiscordWebhook, DiscordEmbed
import keep_alive
keep_alive.keep_alive()
webhook_url = 'WEBHOOK_URL_HERE'
user_string = string.ascii_letters + "_"
user_value = 5

while True:
    try:
        char_list = list(user_string)
        char = random.choices(char_list, k=user_value)
        
        username = "".join(char)
        result = requests.get(f"https://auth.roblox.com/v1/usernames/validate?request.username={username}&request.birthday=1969%2F04%2F20&request.context=Signup").json()
        if int(result["code"]) == 0:
            print(result["message"]+": " +username)
            
            time.sleep(1.50)
            
            webhook = DiscordWebhook(url=webhook_url)
            
            embed = DiscordEmbed(title='Username Generator', description=f'{username}', color='ff2050')
            
            webhook.add_embed(embed)
            
            response = webhook.execute()
            with open("usernames.txt", "a") as f:
                f.write(username + "\n")
        elif int(result["code"]) != 0:
            print(result["message"] + ": " +username)
    except:
        pass
