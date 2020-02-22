import discord
import config
client = discord.Client()



@client.event
async def on_ready():
	print('Bot is ready')

@client.event
async def on_message(msg):
	print(msg.author.name)


client.run('NjgwODQwNDczOTc1NTg2OTkz.XlFz-A.aDtEKtDhI0X2vssCKz7q5VNIC8w')