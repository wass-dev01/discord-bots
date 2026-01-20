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
import wavelink

token=("")



intents = discord.Intents().all()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", description="Jupiter, Terre !!!!", intents=intents)
bot.remove_command('help')



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type= discord.ActivityType.watching, name="Jupiter, Terre !!!!"))
    print("Jupiter, Terre !!!")



#Système welcome
@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(873569504335114252)
    embed = discord.Embed(title="Il y a du rafue sur Ikaru", description="Bienvenue à " + "{}".format(member.mention) + "au **Ikaru World**", color=0xecf0f1,timestamp=datetime.now())
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/951919811737292824/1097323062027886725/jupiter_terre.png')
    await channel.send(embed=embed)
    role = discord.utils.get(member.guild.roles, name = "✏️𝗺𝗲𝗺𝗯𝗿𝗲✏️")
    await member.add_roles(role)

#Commande de modération

@bot.command()
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(title="LE SALON EST CLEAN", color=0x3498db, timestamp=datetime.now())
    await ctx.send(embed=embed, delete_after=1)
    channel = bot.get_channel(873568958475796500)
    await channel.send(embed=embed)

@bot.command()
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title="Un membre a été banni d'Ikaru...", description="{}".format(member.mention) + " a été ban du serveur pour la raison suivante: " + "**{}**".format(reason), color=0xe74c3c, timestamp=datetime.now())
    await ctx.send(embed=embed)
    channel = bot.get_channel(873568958475796500)
    await channel.send(embed=embed)

@bot.command()
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title="Jupiter a kick un utilisateur", description="{}".format(member.mention) + " a été kick du serveur pour la raison suivante: " + "**{}**".format(reason), color=0xe67e22, timestamp=datetime.now())
    await ctx.send(embed=embed)
    channel = bot.get_channel(873568958475796500)
    await channel.send(embed=embed)

@bot.command()
async def unban(ctx, *, member):
    banned_users = ctx.guild.bans()
    member_name = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user   

        if(user.name, user.discriminator) == (member_name):
            await ctx.guild.unban(user)
            embed = discord.Embed(title="Un banni revient a Ikaru World...", description=f"{user.mention} est de retour", color=0x2ecc71)
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
        if select.values[0] == "Règlement":
            await interaction.response.send_message("[BUG ACTUEL]")
        await interaction.response.send_message("[CETTE COMMANDE EST EN COURS DE PROGRAMMATION]")

@bot.command()
async def servmenu(ctx):
    await ctx.send("**Serv' Menu**", view=MyView2())


@bot.command()
async def helptick(ctx):
    embed = discord.Embed(title="TICKETS 📩", description="Afin d'utiliser les tickets vous devez bien les renseignés en respectant une certaine syntaxe.", color=0x2ecc71) 
    embed.add_field(name="Comment rédiger un ticket ?", value="Pour crée un ticket vous devez utilisé la commande **!ticket** suivi de votre id sous la forme [@monid#0000] puis de la raison de votre ticket. La raison de ce dernier doit être explicite est le plus clair possible.")
    await ctx.send(embed=embed)


@bot.command()
async def create(ctx):
    guild = ctx.message.guild
    await guild.create_text_channel('Tickets')

@bot.command()
async def delete(ctx, channel: discord.TextChannel):
    await channel.delete()

#NON FINI
@bot.command()
async def ticket(ctx,member: discord.Member, *, reason=None):
    channel = bot.get_channel(873568958475796500)
    embed = discord.Embed(title=f"Un nouveau ticket a été crée.", description=f"L'utilisateur:"+ "{}".format(member.mention) + f" a crée un ticket pour la raison suivante **{reason}**", color=0xecf0f1, timestamp=datetime.now() )
    await channel.send(embed=embed)
    member= ctx.author
    guild = ctx.message.guild
    overwrites = discord.PermissionOverwrite()
    overwrites.send_messages = False
    overwrites.read_messages = True
    await guild.create_text_channel('Ticket de ' + '{}'.format(member), overwrites=overwrites)
    role_name = "Ticket de " + '{}'.format(member)
    await guild.create_role(name=role_name)
    await member.add_roles(role_name)


class Ikaru(discord.ui.View):
    @discord.ui.select(
        placeholder = "IKARU",
        min_values = 1, 
        max_values = 1, 
        options = [ 
            discord.SelectOption(
                label="HELP ☁️",
                description="Toute les commandes disponibles sur le serveur."
            ),
            discord.SelectOption(
                label="REGLEMENT ✅",
                description="Vous retrouverez l'intégralité du règlement si besoin. [NON DISPONIBLE]"
            ),
            discord.SelectOption(
                label="MUSIQUE 🎵",
                description="Commande de musiques. [NON DISPONIBLE]"
            ),
            discord.SelectOption(
                label="JEUX 🕹️",
                description="Commande de jeux. [NON DISPONIBLE]"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "REGLEMENT":
            await interaction.response.send_message("[BUG ACTUEL]")
        elif select.values[0] == "HELP ☁️":
            embed = discord.Embed(title="HELP", description="Vous retrouverez ici les commandes disponible sur le serveur.", color=0x2ecc71)
            embed.add_field(name="!clear", value="Cette commande nettoite le chat.", inline=False)
            embed.add_field(name="!ban", value="Banni une personne du serveur", inline=False)
            embed.add_field(name="!kick", value="Kick une personne du serveur", inline=False)
            embed.add_field(name="!addrole", value="Ajouter un rôle à une personne", inline=False)
            embed.add_field(name="!removerole", value="Enlève un rôle à une personne", inline=False)
            await interaction.response.send_message(embed=embed)
        await interaction.response.send_message("[CETTE COMMANDE EST EN COURS DE PROGRAMMATION]")

@bot.command()
async def HELPP(ctx):
    await ctx.send("**🚀IKARU🚀**", view=Ikaru())

@bot.command()
async def role(ctx):
    channel = bot.get_channel(1097301086127267840)
    embed = discord.Embed(title="Vos rôles", description="Merci de séléctionner les réactions ci-dessous pour pouvoir continuer a vous balader sur IKARU", color=0xbdc3c7)
    moji = await channel.send(embed=embed)
    await moji.add_reaction('🟢')
    await moji.add_reaction('🚀')
    await moji.add_reaction('🕹️')

@bot.event
async def on_reaction_add(reaction, user):
    Channel = bot.get_channel(1097301086127267840)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "🟢":
      Role = discord.utils.get(user.guild.roles, name="🌴chillman🌴")
      await user.add_roles(Role)
    elif reaction.emoji == "🚀":
      Role = discord.utils.get(user.guild.roles, name="🎮gamer🎮")
      await user.add_roles(Role)
    elif reaction.emoji == "🕹️":
      Role = discord.utils.get(user.guild.roles, name="🕹️")
      await user.add_roles(Role)

@bot.event
async def on_reaction_remove(reaction, user):
    Channel = bot.get_channel(1097301086127267840)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "🟢":
      Role = discord.utils.get(user.guild.roles, name="🌴chillman🌴")
      await user.remove_roles(Role)
    elif reaction.emoji == "🚀":
      Role = discord.utils.get(user.guild.roles, name="🎮gamer🎮")
      await user.remove_roles(Role)
    elif reaction.emoji == "🕹️":
      Role = discord.utils.get(user.guild.roles, name="🕹️")
      await user.remove_roles(Role)




bot.run(token)