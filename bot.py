import discord
from discord.ext import commands
import os,sys
lib_path = os.path.abspath(os.path.join('src'))
sys.path.append(lib_path)
client = commands.Bot(command_prefix = '.')
from getWeather import *
from getCovid import *
from getNew import *
@client.event
async def on_ready():
    print('Bot is ready')
    #print(client.user)
    print('We have logged in as {0.user}'.format(client))
#@client.event
#async def on_message(message):
    #if message.author == client.user:
        #return

    #if message.content.startswith('$hello'):
        #await message.channel.send('Hello!') 
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')
@client.command()
async def covid(ctx,arg):
    tb = getCovid(arg)
    await ctx.send(tb)
@client.command()
async def weather(ctx,arg):
    tb = getWeather(arg)
    await ctx.send(tb)
@client.command()
async def new(ctx):
    url_list = getURL()
    for i in url_list:
        await ctx.send(i)
# Your token
Your_token = ''
client.run(Your_token)
