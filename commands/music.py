import discord
from discord.ext import commands
from commands.base_command import BaseCommand
import youtube_dl
import os

class Play(BaseCommand):
    def __init__(self):
        description = "Muziko Hrej"
        params = ["url"]
        super().__init__(description,params)
    
    async def handle(self, params, message, client):
        ctx = None
        url = params[0]
        song_there = os.path.isfile("song.mp3")
        try:
         if song_there:
            os.remove("song.mp3")
        except PermissionError:
           await ctx.send("Wait for the current playing music to end or use the 'stop' command")
           return
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
        await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
         'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))





