from discord.ext import commands
from math import prod

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['+'])
    async def add(self, ctx, *nums : int):
        """Adds numbers together (seperate numbers by spaces)."""
        await ctx.reply(sum(nums))
    
    @commands.command(aliases=['-', 'subtract'])
    async def sub(self, ctx, *nums : int):
        """Subtracts numbers (seperate numbers by spaces)."""
        if len(nums) > 1:
            await ctx.reply(nums[0]-sum(nums[1:]))
        elif len(nums) == 1:
            await ctx.reply(nums[0])
    
    @commands.command(aliases=['*', 'multiply'])
    async def mult(self, ctx, *nums : int):
        """Multiplys numbers together (seperate numbers by spaces)."""
        await ctx.reply(prod(nums))
    
    #TODO add divide function
    
    