import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
from commands.calculator import Calculator
from commands.tools import Tools
from commands.fun import Fun

# Load tokens / api keys
load_dotenv()
DISCORD_TOKEN = getenv('DISCORD_TOKEN')
WEATHER_TOKEN = getenv('WEATHER_TOKEN')
CAT_TOKEN = getenv('CAT_TOKEN')

# Change only the no_category default string
help_command = commands.DefaultHelpCommand(
    no_category = 'Miscellaneous',
    dm_help = True
)

# Create bot instance
smid = commands.Bot(command_prefix='s!', 
                    description="Hi! My name is Smid the S'more. #Hackbeanpot2021!\nHere are my commands:",
                    help_command=help_command)

# Prints message after succesfully logging in, sets activity
@smid.event
async def on_ready():
    print('Logged in as {0.user.name} #:{0.user.id}!'.format(smid))
    await smid.change_presence(activity = discord.Activity(
                          type = discord.ActivityType.watching, 
                          name = 'the campfire'))
# General error handling          
@smid.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.reply('Invalid input. Please try again.')
    else:
        await ctx.reply('An error has occurred. Please try again.')

# Add categories (along with their commands) to bot
smid.add_cog(Calculator(smid))
smid.add_cog(Fun(smid, CAT_TOKEN))
smid.add_cog(Tools(smid, WEATHER_TOKEN))

# Launch bot
smid.run(DISCORD_TOKEN)


