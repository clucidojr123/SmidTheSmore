from discord.ext import commands
from math import prod

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['+'])
    async def add(self, ctx, *nums : float):
        """Adds numbers together (separate numbers by spaces)."""
        await ctx.reply(sum(nums))
    
    @commands.command(aliases=['-', 'subtract'])
    async def sub(self, ctx, *nums : float):
        """Subtracts numbers (separate numbers by spaces)."""
        if len(nums) > 1:
            await ctx.reply(nums[0]-sum(nums[1:]))
        elif len(nums) == 1:
            await ctx.reply(nums[0])
    
    @commands.command(aliases=['*', 'multiply'])
    async def mult(self, ctx, *nums : float):
        """Multiplys numbers together (separate numbers by spaces)."""
        await ctx.reply(prod(nums))
    
    @commands.command(aliases=['/', 'div', 'quotient'])
    async def divide(self, ctx, numerator : float, denominator : float):
        """Divides numbers together (separate numbers by spaces)."""

        # Return quotient unless denominator is 0
        if(denominator == 0):
            raise commands.BadArgument()
        else:
            await ctx.reply(numerator / denominator)
    
    