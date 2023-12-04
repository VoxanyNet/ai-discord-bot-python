import json

from bot import AIBot

with open("settings.json", "r") as file:
    settings = json.load(file)

bot = AIBot()

bot.run(settings["token"])