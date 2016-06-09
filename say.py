import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix=['.'])

@bot.command(pass_context=True)
async def say(ctx):
    await bot.say(ctx.message.content.split(' ', 1)[1])
    
 @bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('token')
