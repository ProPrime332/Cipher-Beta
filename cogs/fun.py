import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.errors import *
import random
import pyfiglet

class fun(commands.Cog):
    " " " Fun commands to enjoy the bot " " "

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'choose', help = 'Settles the score someway')
    async def choose(self, ctx, *choices):
        " " " Settles the score someway " " "
        await ctx.send(random.choices(choices))

    @commands.command(name='kill', help='Gives a random kill response.')
    async def kill(self, ctx, *, user):
        " " " Gives a random kill response. " " "
        await ctx.send(f"Ooh you killed {user}")

    @commands.command(name='dm')
    async def dm(self, ctx, user : discord.User,  *, message):
        " " " Sends the specified user a DM. " " "
        await user.send(f'{ctx.author} sent you a message read it pls *:{message}*')
        await ctx.send(f'Sent a message to {user}')

    @commands.command(name='wow')
    async def wow(self, ctx):
        " " " Sends a WOW gif. " " "
        await ctx.send('https://tenor.com/view/wow-ted-gif-4233186')

    @commands.command(name='ascii')
    async def  ascii(self, ctx, *, inp : str):
    	inp = pyfiglet.figlet_format(inp)
    	await ctx.send(f'```{inp}```')

def setup(bot):
    bot.add_cog(fun(bot))
