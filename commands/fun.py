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
    
        
