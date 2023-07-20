import pyautogui as pg
import keyboard as kb
from discord import SyncWebhook

while True:
        print("starting...")
        break
fh = open('text.txt')
for line in fh:
    pg.sleep(3)
    webhook = SyncWebhook.from_url("discord webhook url here")
    webhook.send(line)
fh.close()


