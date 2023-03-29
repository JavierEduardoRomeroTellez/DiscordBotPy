from turtle import title
import discord
import datetime
from discord.ext import commands
#from urllib import parse, request
#from NHentai import NHentai
#import re
import music
import random
import requests
import json

Cog = [music]

# Esto es para dar la bienvenida, son como permisos del bot de Discord para poder interactuar con el SV y los miembros
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='>',
                   description="Un bot bien verga", intents=intents)  # Se carga aqui

for i in range(len(Cog)):
    Cog[i].setup(bot)


@bot.command()
async def ping(ctx):
    await ctx.send('México desperto cabrones')


@bot.command()
async def sum(ctx, one: int, two: int):
    await ctx.send(one + two)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Pinche bot bien programado alv",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://c.tenor.com/VU9RgGX08DIAAAAC/globama-obama.gif")
    await ctx.send(embed=embed)


@bot.command()
async def pito(ctx, *, search):
    busqueda_mamalona = parse.urlencode({'search_query': search})
    html_content = request.urlopen(
        'https://www.youtube.com/results?' + busqueda_mamalona)
    resultados_mamalones = re.findall(
        'watch\?v=(.{11})', html_content.read().decode('utf-8'))
    # print(resultados_mamalones)
    await ctx.send('http://www.youtube.com/watch?v=' + resultados_mamalones[0])

# Comando de chichis
@bot.command(name='chiches', aliases=['boobs', 'chichis'])
async def nhentai(ctx):
    await ctx.send('Tenga sus chichis señor')
    response = requests.get('http://api.nekos.fun:8080/api/boobs')
    result = response.json()
    await ctx.send(result['image'])

# Comando de hentai
@bot.command(name='hentaii', aliases=['h', 'hentai'])
async def nhentai(ctx):
    await ctx.send('Veo que eres un hombre de cultura')
    response = requests.get('http://api.nekos.fun:8080/api/hentai')
    result = response.json()
    await ctx.send(result['image'])

# Comando de cum
@bot.command(name='cumm', aliases=['cum', 'cumming'])
async def nhentai(ctx):
    response = requests.get('http://api.nekos.fun:8080/api/cum')
    result = response.json()
    await ctx.send(result['image'])

# Comando de nalgadas
@bot.command(name='spanks', aliases=['nalgadas', 'spank'])
async def nhentai(ctx):
    await ctx.send('Veo que eres un hombre de cultura')
    response = requests.get('http://api.nekos.fun:8080/api/spank')
    result = response.json()
    await ctx.send(result['image'])

# Events


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Me pela la verga Tony Stark"))
    print('México desperto cabrones')

# Anunciar bienvenida


@bot.event
async def on_member_join(member):
    print(f"{member} se ha unido al show")
    welcome_channel = bot.get_channel(996294619723747378)
    await welcome_channel.send(f"{member.mention} se ha unido al show! :hot_face: :point_right::ok_hand: :sweat_drops:")

# Anunciar salida


@bot.event
async def on_member_remove(member):
    print(f"{member} se fue a la verga")
    msgs = ['sisisisi, que se vaya!', 'Se fue un joto', 'Ni quien te queria aqui',
            'Te ira mejor en el bote', 'Este wey era simpatizante de AMLO']
    welcome_channel = bot.get_channel(996296050606362714)
    await welcome_channel.send(f"{member.mention}" + random.choice(msgs))


# Quitar el Token antes de subir a GIT XD
bot.run('OTk1MDk1ODMyNzg3NDM5Njc2.GAATyf.w3-Qo77icy4b6WE09TAFl1v5dY8fevfJ4Mmfs4')
