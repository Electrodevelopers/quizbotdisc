import discord
client = discord.Client()

import config.py
import lobby.py


@client.event
async def on_ready():
	print('Bot is ready')

@client.event
async def on_message(msg):
	print(msg.author.name)


client.run(token)