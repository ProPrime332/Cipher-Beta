import discord
from discord.ext import commands
import math

class math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add', help = 'Adds 2 given numbers.')
    async def asu(self, ctx, number1 : int, number2 : int):
        su=(number1 + number2)
        await ctx.send(su)

    @commands.command(name='multiply', aliases = ['mult', 'multi', 'product'], help = 'Multiplies 2 given numbers.')
    async def mult(self, ctx, number1 : int, number2 : int):
        su=(number1 * number2)
        await ctx.send(su)

    @commands.command(name='difference', aliases = ['subtract', 'minus', 'diff'], help = 'Subtracts 2 given numbers.')
    async def add(self, ctx, number1 : int, number2 : int):
        su=(number1 - number2)
        await ctx.send(su)

    @commands.command(name='odd-even', aliases=['odd', 'even'])
    async def odeve(self, ctx, number : int):
        if number % 2 == 0 :
            await ctx.send('Your Number is even')
        else:
            await ctx.send('Your Number is odd')

def setup(bot):
    bot.add_cog(math(bot))
