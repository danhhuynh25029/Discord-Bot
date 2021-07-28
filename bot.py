import discord
import youtube_dl
from discord import colour
from discord.ext import commands
import os,sys
lib_path = os.path.abspath(os.path.join('src'))
sys.path.append(lib_path)
client = commands.Bot(command_prefix = '.')
from getWeather import *
from getCovid import *
from getNew import *
from getAnime import *
@client.event
async def on_ready():
    # await ctx.send("Bot da tro lai roi")
    print('Bot is ready')
    #print(client.user)
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')
@client.command()
async def covid(ctx,arg):
    if arg == "":
        arg = "all"
    tb = getCovid(arg)
    if len(tb) > 1:
        for tmp in tb:
            embed = discord.Embed(
            title = tmp[0],
            discription = "This is discription",
            color=discord.Color.blue()
            )
            embed.add_field(name="Country",value=tmp[1],inline=True)
            embed.add_field(name="TotalConfirmed",value=str(tmp[2]),inline=True)
            embed.add_field(name="TotalDeaths",value=str(tmp[3]),inline=True)
            await ctx.send(embed=embed)
    else:
        tmp = tb[0]
        embed = discord.Embed(
            title = tmp[0],
            discription = "This is discription",
            color=discord.Color.blue()
        )
        embed.add_field(name="Country",value=tmp[1],inline=True)
        embed.add_field(name="TotalConfirmed",value=str(tmp[2]),inline=True)
        embed.add_field(name="TotalDeaths",value=str(tmp[3]),inline=True)
        await ctx.send(embed=embed)
@client.command()
async def weather(ctx,arg):
    if arg == "":
        arg = "Tra_Vinh"
    tb = getWeather(arg)[0]
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    embed.add_field(name="city",value=tb[0],inline=True)
    embed.add_field(name="description",value=tb[1],inline=True)
    embed.add_field(name="temp",value=tb[2],inline=True)
    await ctx.send(embed=embed)
@client.command()
async def new(ctx):
    url_list = getURL()
    for i in url_list:
        await ctx.send(i)
@client.command()
async def anime(ctx,arg):
    url_list = getListAnime(arg)
    for i in url_list:
        await ctx.send(i)
@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)
@client.command()
async def happy(ctx,arg):
    await ctx.send("happy birthday "+":birthday: "+arg)
# @client.command(pass_context=True)
# async def play(ctx,url):
#     server = ctx.message.server
#     voice = client.voice_client_in(server)
#     player = await voice.create_ytdl_player(url)
#     players[server.id] = player
#     player.start()
# @client.commnad()
# Your token
Your_token = ''
client.run(Your_token)
