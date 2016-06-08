import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix=['.'])

@bot.command(pass_context=True)
async def flipcoin(ctx):
    if ctx.message.content == '.flipcoin':
        pick = ['heads','tails']
        flip = random.choice(pick)
        await bot.say ("The coin landed on " + flip + '!')
        
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('token')
