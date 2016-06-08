import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix=['.'])

@bot.command(pass_context=True)
async def roll():
    if ctx.message.content == '.roll':
        roll = random.randint(1, 100)
        await bot.say("Your number is " + str(roll))
        
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('token')
