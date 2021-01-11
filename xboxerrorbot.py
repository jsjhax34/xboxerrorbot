import discord
from discord.ext import commands
import json
with open('xerr.json', 'w') as xerrjson:
    xerr = json.load(xerrjson)
TOKEN = 'lolno'
PREFIX = 'x!'
INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix='x!', intents=INTENTS)


@bot.command()
async def ping(ctx):

    await ctx.send('Pong!')

#funny code owo
@bot.command
async def error(ctx,*args):
    errorcode = args[0]
    if errorcode in xerr:
        errordata = xerr[errorcode]
    else:
        errordata = xerr['fallback']
    info = errordata['explanation']
    await ctx.send(info)

bot.run(TOKEN)