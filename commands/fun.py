from discord.ext import commands
import requests

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['funfact', 'funFact'])
    async def fact(self, ctx):
        """Returns a random fun fact."""
        # call API
        res = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")

        # Send proper response depending on request status
        if(res.status_code != 200):
            await ctx.reply('An error has occurred. Sorry!')
        else:
            data = res.json()
            await ctx.reply(data['text'])

    @commands.command(aliases=['roast', 'nice', 'comp'])
    async def compliment(self, ctx):
        """Returns a random compliment."""

        # call API
        res = requests.get("https://complimentr.com/api")

        # Send proper response depending on request status
        if(res.status_code != 200):
            await ctx.reply('An error has occurred. Sorry!')
        else:
            data = res.json()
            await ctx.reply(data['compliment'])
    
    @commands.command(aliases=['laugh', 'dadjoke'])
    async def joke(self, ctx):
        """Returns a random joke."""
        
        # call API
        res = requests.get("https://official-joke-api.appspot.com/jokes/random")

        # Send proper response depending on request status
        if(res.status_code != 200):
            await ctx.reply('An error has occurred. Sorry!')
        else:
            data = res.json()
            await ctx.reply(data['setup'] + "\n\n" + f"||{data['punchline']}||")
    
        
