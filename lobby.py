@client.event
async def on_message(msg):
	for i in msg.author.roles:
		print(i)