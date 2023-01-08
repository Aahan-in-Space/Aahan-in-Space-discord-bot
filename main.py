import os
import discord
from bot_always_online import always_online

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Hey guys I have finally been created! There is a test user ID of me below!")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send(message.content[::-1])

my_secret = os.environ["token"]
always_online()
client.run(my_secret)