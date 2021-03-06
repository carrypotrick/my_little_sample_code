from google_images_download import google_images_download
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt
import os
import time
import random as rd

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print('connected')
    await bot.change_presence(activity = discord.Game('짤 생성 노가다'))
    
@bot.command()
async def 짤(ctx, *context):
    response = google_images_download.googleimagesdownload()
    
    wannakeywords = ''
    for i in range(0, len(context)):
        wannakeywords += str(context[i]) + ' '
    
    wannakeywords = wannakeywords[: -1]
    arguments = {'keywords' : wannakeywords, 'limit' : 5, 'print_urls' : True}

    paths = response.download(arguments)
    
    
    file_path = os.listdir(os.getcwd() + '/downloads/' + wannakeywords)
    await ctx.send(file = discord.File(os.getcwd() + '/downloads/' + wannakeywords + '/' + file_path[rd.randint(0, 4)]))
    
    for wannafile in file_path:
        
        os.remove(os.getcwd() + '/downloads/' + wannakeywords + '/' + wannafile)
        
    os.rmdir(os.getcwd() + '/downloads/' + wannakeywords)
    
    
@bot.event
async def on_message(message):
    if message.guild:
        async for message in message.channel.history():
            if '!짤' in message.content:
                try:
                    await bot.process_commands(message)
                    await message.delete()
                except:
                    pass
                await asyncio.sleep(0.5)

    
    
access_token = os.environ['BOT_TOKEN']    
bot.run(access_token)
