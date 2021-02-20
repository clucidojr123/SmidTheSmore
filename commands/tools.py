from discord.ext import commands
from random import randint


class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['roll'])
    async def dice(self, ctx, num : int):
        """Rolls a user-input-sided dice (default 6 sides)."""
    
        # Check if number input is valid, send proper response
        if(num <= 1):
            await ctx.reply('Invalid input number. Please try again.')
        else:
            await ctx.reply(randint(1, num))