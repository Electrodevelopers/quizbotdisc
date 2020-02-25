import discord,asyncio,config,questions,random
client = discord.Client()
global game
game = False
global games
games = False
global users
users = []
global ans 
ans = ''
global uans
uans = []
global usga
usga = []
def endgame():
	global game
	game = False
	global games
	games = False
	global users
	users = []
	global ans
	ans = ''
	global uans
	uans = []
	global usga
	usga = []
def stg():
	global game
	game = True
async def testusersa(ch):
	global uans
	for i in users:
		if(i not in uans):
			users.remove(i)
			print(users)
			await ch.send('{0} выбывает из игры!'.format(client.get_user(i).name))
		if(i in uans):
			await ch.send('{0} дает правильный ответ!'.format(client.get_user(i).name))
async def waitans(ch):
	global users
	print(str(len(users)) + 'waitans f')
	if(len(users) != 1):
		await asyncio.sleep(10)
		await testusersa(ch)
		await sendquestion(ch)
	elif(len(users) == 1):
		await ch.send('{0} выиграл игру!'.format(client.get_user(users[0])))
	elif(len(users) == 0):
		await ch.send('Никто не выигрывает игру!')
async def sendquestion(ch):
	global users
	print(str(len(users)) + 'sendq f')
	if(len(users) != 1):
		global ans 
		global usga
		global uans
		uans = []
		usga = []
		quen = random.randint(0,len(questions.que)-1)
		await ch.send(questions.que[quen][0] + '\n У вас есть 10 секунд!')
		ans = questions.que[quen][1]
		await waitans(ch)
	elif(len(users) == 1):
		await ch.send('{0} выиграл игру!'.format(client.get_user(users[0])))
		endgame()
	elif(len(users) == 0):
		await ch.send('Никто не выигрывает игру!')
		endgame()
async def startquiz(ch):
	await asyncio.sleep(30)
	global users
	global games
	if(len(users) == 1 or len(users) == 0):
		users = []
		global game
		game = False
		games = False
		global ans
		ans = ''
		global uans
		uans = []
		await ch.send('Для игры нужно более двух человек')
	else:
		await ch.send('Викторина начинается!\n Когда задается вопрос, вы ОБЯЗАНЫ дать ответ, после того, как вы дали ответ, вы можете продолжать общение')
		games = True
		await sendquestion(ch)
@client.event
async def on_ready():
	print('Bot is ready')

@client.event
async def on_message(msg):
	roles = []
	if(str(msg.channel) == 'викторина-бот'):
		for i in msg.author.roles: #Get roles of author
			roles.append(str(i.name))
		global game
		global games
		global ans
		global users
		global usga
		if('мастер викторины' in roles):  #If author is administratorcmd
			if(str(msg.content) == 'Qstart' and game == False and games == False):
				ch = msg.channel
				await ch.send('Викторина начнется через 30 секунд. Подключайтесь через команду "Qjoin"')
				stg()
				await startquiz(msg.channel)
		if(str(msg.content) == 'Qjoin' and game == True and msg.author.id not in users and games == False):
			await msg.channel.send('{0} присоединяется к игре!'.format(msg.author.name))
			users.append(msg.author.id)
		if(games==True and game == True and msg.author.id in users and str(msg.content) == ans and msg.author.id not in usga):
			uans.append(msg.author.id)
			usga.append(msg.author.id)

client.run('NjgwODQwNDczOTc1NTg2OTkz.XlF3Gw.xK7URob87SFm06nADkZ029XNRCo')