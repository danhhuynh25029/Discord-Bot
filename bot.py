import discord
from discord.ext import commands
import os,sys
lib_path = os.path.abspath(os.path.join('src'))
sys.path.append(lib_path)
client = commands.Bot(command_prefix = '.')
from getWeather import *
from getCovid import *
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
#client.run('ODY4MzEzOTYwMDQ1MjMyMTY4.YPt2ZA.CxOlhroSr7vC4ALA7bqQrPiB_sY')
