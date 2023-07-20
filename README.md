# text-to-discord-webhook
this code will help you send line by line from a text file to discord webhook every 3 seconds

## another way to use
- **if you whant to send a random image api you can change to this**. 
   ```
    import requests
    import base64
    import time
    import json
    import discord
    from discord import SyncWebhook

    print("starting...")
    while True:
        mp = requests.get("https://api.thedogapi.com/v1/images/search").json()
        print(mp)
        webhook = SyncWebhook.from_url("your discord webhook url")
        webhook.send(mp)
        time.sleep(3)
free anime images api here > https://www.nekos.fun/apidoc.html <


