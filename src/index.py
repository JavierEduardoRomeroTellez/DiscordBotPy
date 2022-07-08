from turtle import title
import discord
import datetime
from discord.ext import commands
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="Un bot bien verga")

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
async def p(ctx, *, search):
    busqueda_mamalona = parse.urlencode({'search_query': search})
    html_content = request.urlopen('https://www.youtube.com/results?' + busqueda_mamalona)
    resultados_mamalones = re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    #print(resultados_mamalones)
    await ctx.send('http://www.youtube.com/watch?v=' + resultados_mamalones[0])

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Me pela la verga Tony Stark"))
    print('México desperto cabrones')

bot.run('OTk1MDk1ODMyNzg3NDM5Njc2.GesJoT.nEcavKOls9kzXzW1SpkU-qPXW-WnxQ7NXJsHeM')