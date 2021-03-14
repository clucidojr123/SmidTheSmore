from discord.ext import commands
from discord import Embed
import requests

class Fun(commands.Cog):
    def __init__(self, bot, CAT_TOKEN):
        self.bot = bot
        self.CAT_TOKEN = CAT_TOKEN
    
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

        
    @commands.command(aliases=['doge', 'doggie', 'pup', 'puppy'])
    async def dog(self, ctx, *, breed=""):
        """Returns a random dog image (within an optional specified breed)."""
        
        # call API
        if(not breed):
            res = requests.get("https://dog.ceo/api/breeds/image/random")
        else:
            res = requests.get("https://dog.ceo/api/breed/{0}/images/random".format(breed.lower()))

        # Send proper response depending on request status
        data = res.json()

        if(data["status"] == "error"):
            await ctx.reply('An error has occurred: ' + data["message"] + 
            ", see https://dog.ceo/dog-api/documentation/ for a list of all breeds.")
        else:
            if breed:
                breed = f" ({breed})"
            newEmbed = Embed(title="🐕" + breed, 
                            color=0x964B00)
            newEmbed.set_image(url=data["message"])
            await ctx.reply(embed=newEmbed)
    

    @commands.command(aliases=['feline'])
    async def cat(self, ctx):
        """Returns a random cat image."""
        
        # call API
        res = requests.get(f"https://api.thecatapi.com/v1/images/search?api_key={self.CAT_TOKEN}")
    
        # Send proper response depending on request status
        if(res.status_code != 200):
            await ctx.reply('An error has occurred. Please try again (Note: There is no breed option for the cat command).')
        else:
            data = res.json()

            newEmbed = Embed(title="🐈", 
                            color=0x964B00)
            newEmbed.set_image(url=data[0]["url"])
            await ctx.reply(embed=newEmbed)
    
    @commands.command(aliases=['pogchamp', 'pog'])
    async def poggers(self, ctx):
        """Returns a poggers gif."""
        newEmbed = Embed(title="Pog", 
                        color=0x964B00)
        newEmbed.set_image(url="https://media1.tenor.com/images/b176db6a7358ea86acc241b3cfa45c3d/tenor.gif")
        await ctx.reply(embed=newEmbed)
        

            
    
        
