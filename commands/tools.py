from discord.ext import commands
from discord import Embed
from random import randint
import requests


class Tools(commands.Cog):
    def __init__(self, bot, token):
        self.bot = bot
        self.token = token

    @commands.command(aliases=['roll'])
    async def dice(self, ctx, num = 6):
        """Rolls a user-input-sided dice (default 6 sides)."""
    
        # Check if number input is valid, send proper response
        if(num <= 1):
            await ctx.reply('Invalid input number. Please try again.')
        else:
            await ctx.reply(randint(1, num))

    @commands.command()
    async def weather(self, ctx, *, location : str):
        """Provides weather information about a certain area"""

        # Call API
        res = requests.get("http://api.weatherstack.com/current?access_key={0}&query={1}".format(self.token, location))

        # Respond to user
        if res.status_code == 104:
            await ctx.reply("We reached the max API calls for this month, sorry!")
        elif res.status_code != 200:
            await ctx.reply("There was an error when retrieving the data. Please try again.")
        else:
            data = res.json()
            newEmbed = Embed(title=data['location']['name'] + " Weather", 
                            color=0x964B00)
            newEmbed.set_thumbnail(url=data['current']['weather_icons'][0])
            temp = int((data['current']['temperature'] * 1.8) + 32)
            newEmbed.add_field(name="Temperature", value=str(temp) + "°F", inline=False)
            newEmbed.add_field(name="Condition", value=data['current']['weather_descriptions'][0], inline=False)
            newEmbed.add_field(name="Wind", value=str(data['current']['wind_speed']) + " km/hr", inline=False)
            await ctx.reply(embed=newEmbed)