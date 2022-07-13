from turtle import title
import discord
import datetime
from discord.ext import commands
from urllib import parse, request
import re
from BeautifulSoup import BeautifulSoup
import music
import random

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
    embed.set_thumbnail(
        url="https://c.tenor.com/VU9RgGX08DIAAAAC/globama-obama.gif")
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


@bot.command(name='nhcodes', aliases=['h', 'nh'])
async def nhentai(ctx):
    numero = random.randint(2, 401092)
    parseo = str(numero)
    code = ('https://nhentai.to/g/' + parseo)
    await ctx.send(code)

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}

    request1 = request.Request(code, None, headers)
    response = request.urlopen(request1)
    html_content = response.read()

    resultados_mamalones = re.findall(
        'img width="350" src="https://cdn.nload.xyz/galleries/(.{7})/cover.jpg', html_content.decode('utf-8'))
    print(resultados_mamalones)
    await ctx.send('https://cdn.nload.xyz/galleries/' + resultados_mamalones[0] + '/cover.jpg')
    await ctx.send('Kya')

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
bot.run('Aqui va el token del bot')
