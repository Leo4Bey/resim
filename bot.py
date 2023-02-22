import discord
from discord import app_commands
from discord.ext import commands
from config import *
import asyncio
import os
import openai
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
    
bot = commands.Bot(command_prefix=prefix, intents=intents)


openai.api_key = (apikey)

@bot.tree.command(name="çiz", description="tarif ettiğiniz şeyi çizet")
@app_commands.describe(tarif = "tarif et ingilizce lütfen")
async def soru(interaction: discord.Interaction, tarif: str):
    await interaction.response.send_message("Bot düşünüyor")

    response = openai.Image.create(
        prompt=tarif,
        n=2,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    await interaction.channel.send(image_url)


@bot.event 
async def on_ready():
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game(name=footer))
    try:
        synced = await bot.tree.sync()
        print(f'Entegre edilen slash Komut sayısı: {len(synced)}')
    except Exception as e:
        print(e)

bot.run(token)
