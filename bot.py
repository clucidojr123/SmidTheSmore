import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
from commands.calculator import Calculator
from commands.tools import Tools
from commands.fun import Fun

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

# Change only the no_category default string
help_command = commands.DefaultHelpCommand(
    no_category = 'Miscellaneous',
    dm_help = True
)

smid = commands.Bot(command_prefix='s!', 
                    description="Hi! My name is Smid. #Hackbeanpot2021!\nHere are my commands:",
                    help_command=help_command)

@smid.event
async def on_ready():
    print('Logged in as {0.user.name} #:{0.user.id}!'.format(smid))
    await smid.change_presence(activity = discord.Activity(
                          type = discord.ActivityType.watching, 
                          name = 'the campfire'))
                        
@smid.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.reply('Invalid input. Please try again.')
    else:
        await ctx.reply('An error has occurred. Please try again.')

smid.add_cog(Calculator(smid))
smid.add_cog(Tools(smid))
smid.add_cog(Fun(smid))

smid.run(TOKEN)


