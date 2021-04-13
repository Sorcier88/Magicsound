import json
import os
import discord
# quotes = json.load(open("engiQuotes.txt"))
voiceQuotes = os.listdir("Sounds/")
token = ""
client = discord.Client()
try:
    # We can't include token.txt in the repository as it is private
    token = os.getenv('TOKEN')
except FileNotFoundError as e:
    print(e)
