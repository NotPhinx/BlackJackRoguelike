import discord
from discord.ext import commands
import nest_asyncio
import os


class BOT(commands.Bot):

    # Define bot parameters
    def init(self):
        super().init(
            command_prefix='>>>',
            intents=discord.Intents.all(),
            application_id=1217310481358917693
        )

#Connect bot to class
client = BOT()
#Connect bot to discord
client.run('f942db1eaacc6d6b51c7839231d61408cff9f7b8bb883c9a7c58731b0e0db27a')