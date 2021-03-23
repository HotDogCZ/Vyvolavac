from commands.base_command import BaseCommand
from utils                 import get_emoji

class Vyvolej(BaseCommand):

    def __init__(self):
        description = "Jak je"
        params = ["kohoVolat", "kolikrát"]
        super().__init__(description, params)
    async def handle(self, params, message, client):
        msg = f"Halooo vole  {params[0]}"
        count = 0
        max = int(params[1]) + 1
        if(max > 20):
            max = 20
        while(count < max):
            await message.channel.send(msg)
            count = count + 1


class Smažíme(BaseCommand):
    def __init__(self):
        description = "Žiješ?"
        params = []
        super().__init__(description, params)
    async def handle(self, params, message, client):
        msg = f"Jdeme smažit!! @everyone"
        count = 0
        while (count < 10):
            await message.channel.send(msg)
            count = count + 1
        await message.channel.send("https://tenor.com/ba4Io.gif") 
        await message.channel.send("https://tenor.com/blBbm.gif") 

class Test(BaseCommand):

    def __init__(self):
        description = "Žiješ?"
        params = []
        super().__init__(description, params)
    async def handle(self, params, message, client):
        msg = f"Žiju vole {message.author.mention}"
        await message.channel.send(msg)

        