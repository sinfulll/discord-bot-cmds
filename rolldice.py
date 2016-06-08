import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix=['.'])

@bot.command(pass_context=True)
async def dice(ctx):
    if ctx.message.content == '.dice':
        num = [':one:',':two:',':three:',':four:',':five:',':six:']
        dice = random.choice(num)
        await bot.say (dice)
        
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('token')
