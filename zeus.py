
from cgitb import text
from imaplib import Time2Internaldate
from sqlite3 import Timestamp
from unicodedata import name
import glob, random
import asyncio
import datetime
import random
from discord.ext import commands
import discord
import time 
from datetime import datetime

token=("")



intents = discord.Intents().all()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", description="ZEUS, the king of the Olympe", intents=intents)
bot.remove_command('help')



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type= discord.ActivityType.watching, name="ZEUS, the king of the Olympe"))
    print("ZEUS a atteint le mont Olympe !")

#Système welcome
@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(1073003095526756383)
    embed = discord.Embed(title="Il y a du nouveau au mont Olympe...", description="Bienvenue à " + "{}".format(member.mention) + "au **Mont Olympe**", color=0xecf0f1,timestamp=datetime.now())
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/951919811737292824/1073687033215725638/logo_serveur.png')
    await channel.send(embed=embed)
    role = discord.utils.get(member.guild.roles, name = "🔱 - OLYMPIEN - 🔱")
    await member.add_roles(role)

#Commande de modération

@bot.command()
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(title="LE SALON EST CLEAN", color=0x3498db, timestamp=datetime.now())
    await ctx.send(embed=embed, delete_after=1)
    channel = bot.get_channel(1073006130235711508)
    await channel.send(embed=embed)

@bot.command()
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title="Un membre a été banni de l'Olympe...", description="{}".format(member.mention) + " a été ban du serveur pour la raison suivante: " + "**{}**".format(reason), color=0xe74c3c, timestamp=datetime.now())
    await ctx.send(embed=embed)
    channel = bot.get_channel(1073006130235711508)
    await channel.send(embed=embed)

@bot.command()
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title="La colère de ZEUS a kick un utilisateur", description="{}".format(member.mention) + " a été kick du serveur pour la raison suivante: " + "**{}**".format(reason), color=0xe67e22, timestamp=datetime.now())
    await ctx.send(embed=embed)
    channel = bot.get_channel(1073006130235711508)
    await channel.send(embed=embed)

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user   

        if(user.name, user.discriminator) == (member_name):
            await ctx.guild.unban(user)
            embed = discord.Embed(title="Un banni revient au Mont Olympe...", description=f"{user.mention} est de retour", color=0x2ecc71)
            await ctx.send(embed=embed)
            return


@bot.command()
async def addrole(ctx, member: discord.Member, *,  role:discord.Role):
    await member.add_roles(role)
    await ctx.send(f'**{member}** a obtenu le role *{role}*')

@bot.command()
async def removerole(ctx, member: discord.Member, *,  role:discord.Role):
    await member.remove_roles(role)
    await ctx.send(f"**{member}** n'a plus le role *{role}*")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="HELP", description="Vous retrouverez ici les commandes disponible sur le serveur.", color=0x2ecc71)
    embed.add_field(name="!clear", value="Cette commande nettoite le chat.", inline=False)
    embed.add_field(name="!ban", value="Banni une personne du serveur", inline=False)
    embed.add_field(name="!kick", value="Kick une personne du serveur", inline=False)
    embed.add_field(name="!addrole", value="Ajouter un rôle à une personne", inline=False)
    embed.add_field(name="!removerole", value="Enlève un rôle à une personne", inline=False)
    await ctx.send(embed=embed)

class MyView(discord.ui.View):
    @discord.ui.button(label="HELP", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        embed = discord.Embed(title="HELP", description="Vous retrouverez ici les commandes disponible sur le serveur.", color=0x2ecc71)
        embed.add_field(name="!clear", value="Cette commande nettoite le chat.", inline=False)
        embed.add_field(name="!ban", value="Banni une personne du serveur", inline=False)
        embed.add_field(name="!kick", value="Kick une personne du serveur", inline=False)
        embed.add_field(name="!addrole", value="Ajouter un rôle à une personne", inline=False)
        embed.add_field(name="!removerole", value="Enlève un rôle à une personne", inline=False)
        await interaction.response.send_message(embed=embed)

@bot.command()
async def help2(ctx):
    await ctx.send(view=MyView())


class MyView2(discord.ui.View):
    @discord.ui.select(
        placeholder = "Serv Menu",
        min_values = 1, 
        max_values = 1, 
        options = [ 
            discord.SelectOption(
                label="Serv' Menu",
                description="Le Serv' Menu est un menu privé destiné à aider les modérateurs pour les commandes."
            ),
            discord.SelectOption(
                label="Règlement",
                description="Vous retrouverez l'intégralité du règlement si besoin."
            )
        ]
    )
    async def select_callback(self, select, interaction):
        await interaction.response.send_message("[CETTE COMMANDE EST EN COURS DE PROGRAMMATION]")

@bot.command()
async def servmenu(ctx):
    await ctx.send("**Serv' Menu**", view=MyView2())

@bot.slash_command() #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def olympe(ctx): 
    await ctx.respond("⚡Par le trident de Zeus ⚡")

bot.run(token)