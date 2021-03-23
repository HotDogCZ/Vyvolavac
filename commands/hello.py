from commands.base_command import BaseCommand
from utils                  import get_emoji

class Nazdar (BaseCommand):

    def __init__(self): 
        description = "Jak je"
        params = None
        super().__init__(description, params)
    async def handle(self, params, message, client):
        msg = f"{message.author.mention} Čus brácho vole"
        await message.channel.send(msg)

class Čau (BaseCommand):

    def __init__(self): 
        description = "Jak je"
        params = None
        super().__init__(description, params)
    async def handle(self, params, message, client):
        msg = f"{message.author.mention} NESER"
        await message.channel.send(msg)

class Heil (BaseCommand):

    def __init__(self): 
        description = "Turečková approved"
        params = None
        super().__init__(description, params)
    async def handle(self, params, message, client):
        msg = f"Heil {message.author.mention} "
        await message.channel.send(msg)
        await message.channel.send("https://tenor.com/bhtbX.gif")
