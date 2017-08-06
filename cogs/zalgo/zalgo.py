import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import aiohttp
import html
import json
import random

class Zalgo:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def zalgo(self, ctx, user : discord.Member=None):
        """Zalgo the text"""
        # first pull out the .zalgo part of the message
        raw_msg = ' '.join(ctx.message.content.split(' ')[1:])

        zalgo_msg = raw_msg

        await self.bot.delete_message(ctx.message)

        await self.bot.say(zalgo_msg)


def setup(bot):
    n = Zalgo(bot)
    bot.add_cog(n)

