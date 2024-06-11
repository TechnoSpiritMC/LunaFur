import asyncio
import datetime

import discord
from discord.ext import commands
from discord.ui import Select, View

import GameManager
import Roles
import UUIDgen
import auxFX
from auxFX import *

intens = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intens)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("INDEV - Features may not work"), status=discord.Status.online)
    consoleLog(log.debug, f"@{client.user.name} is ready and logged in.")


@client.command()
async def Help(ctx):
    user = ctx.message.author
    await ctx.send(
        """
        **Aide PalaBlacklistBot:**
        
        **help**:
        `!help` - Affiche le panel d'aide
        
        **status**:
        `!status <pseudo>` - Affiche le status d'un joueur
        
        **ping**:
        `!ping` - Affiche le temps de latence du bot
        
        **report**:
        `!report <pseudo> <raison> <date>` - Crée un ticket de signalement
        
        """)
    print()
    consoleLog(log.info, f"@{user.name} Executed command /Help")


# Votre commande game avec les modifications
@client.command()
async def game(ctx, arg0=None, arg1=None, arg2=None, arg3=None):
    user = ctx.message.author

    arg1 = int(arg1)

    if arg0 == "new":
        if arg1 is not None:
            if arg1 >= Roles.Roles.min:
                if arg1 <= Roles.Roles.max:

                    GameID = UUIDgen.generateID()

                    UserEmbed = discord.Embed(
                        title=f"Création d'une partie",
                        description=f"Veuillez suivre et répondre aux questions que le bot va dès-à-présent vous poser, car elles sont importantes pour la création de la partie.",
                        color=0xff1100
                    )

                    UserEmbed.add_field(
                        name="\nAttention:",
                        value="Lors qu le bot va vous demander des pseudos, merci de les donner sous forme de @mention.",
                        inline=False
                    )

                    UserEmbed.add_field(
                        name="\n\n\nA propos de la partie",
                        value=f"Membres maximum: {Roles.Roles.max}\nID: {GameID}",
                        inline=True
                    )

                    UserEmbed.set_footer(text="A propos de moi: Lunafur est un bot de loup garou sur discord développé par Technospirit.")

                    Name = str(user.name)

                    ServerEmbed = discord.Embed(
                        title=f"Création d'une partie",
                        description=f"{Name[0].capitalize()}{Name[1:]} a proposé de démarrer une partie à {arg1}. Réagissez pour rejoindre!",
                        color=0xff1100
                    )

                    ServerEmbed.set_footer(
                        text="Vous pouvez quitter la partie à tout moment jusqu'à ce que l'objectif de réactions soit rempli.")

                    await user.send(embed=UserEmbed)

                    RolesList = ""
                    for i in Roles.Roles.roles.get(str(arg1)).keys():
                        RolesList = RolesList + (i + ": " + str(Roles.Roles.roles.get(str(arg1)).get(i)) + "\n")

                    game_message = await ctx.send(embed=ServerEmbed)
                    await game_message.add_reaction("✅")  # Ajout de la réaction

                    await user.send(embed=discord.Embed(
                        title=f"Information sur la partie:",
                        description=f"**ID de la partie:** {GameID}\n**Nombre de joueurs:** {str(arg1)}\n\n### Rôles:\n{RolesList}",
                        color=0xff1100))

                    consoleLog(log.info,
                               f"@{user.name} Executed command /game {arg0}. Création d'une nouvelle partie d'ID " + GameID)

                    # ---Game Creation---

                    # Attendre les réactions jusqu'à ce que le nombre de réactions corresponde au nombre de joueurs
                    while True:
                        game_message = await ctx.fetch_message(game_message.id)
                        reaction = discord.utils.get(game_message.reactions, emoji="✅")
                        num_reactions = reaction.count - 1  # -1 pour exclure le bot lui-même
                        print(str(GameID) + " → " + str(num_reactions) + "/" + str(arg1) + " | " + str(round((num_reactions/arg1)*100, 1)) + "%.")
                        if num_reactions >= arg1:
                            await ctx.send("Objectif de réactions atteint pour la game " + GameID + "!")
                            break
                        await asyncio.sleep(5)  # Attendre 5 secondes avant de vérifier à nouveau les réactions

                    # Récupération des utilisateurs ayant réagi
                    reacted_users = []
                    async for user in reaction.users():
                        if user != client.user:  # Exclure le bot
                            reacted_users.append(user)

                    # Affichage des utilisateurs ayant réagi
                    print("Utilisateurs ayant réagi : " + str(reacted_users))
                    for user in reacted_users:
                        print(user.name)

                    GM = GameManager.GameManager()
                    GM.AddGame(reacted_users)

                    CGU = GameManager.CGU(reacted_users)
                    
                    await ctx.send("Registered games: " + CGU.get_all_ids())


                else:
                    await user.send(embed=discord.Embed(
                        title=f"Erreur lors de la création de la partie",
                        description=f"Veuillez avoir entre 6 et 11 joueurs dans votre partie!",
                        color=0xff1100), ephemeral=True)

            else:
                await user.send(embed=discord.Embed(
                    title=f"Erreur lors de la création de la partie",
                    description=f"Veuillez avoir entre 6 et 11 joueurs dans votre partie!",
                    color=0xff1100))
        else:
            await user.send(embed=discord.Embed(
                title=f"Erreur lors de la création de la partie",
                description=f"Veuillez renseigner le nombre de joueurs dans la partie que vous voulez créer!",
                color=0xff1100))




@client.command()
async def cpc(ctx):
    # Création du salon texte
    channel = await ctx.guild.create_text_channel('lg')

    # Définition des permissions pour ce salon
    overwrite = discord.PermissionOverwrite()
    overwrite.read_messages = False  # Interdit la lecture des messages
    overwrite.send_messages = False  # Autorise l'envoi de messages

    sender = discord.PermissionOverwrite()
    sender.read_messages = True  # Interdit la lecture des messages
    sender.send_messages = True  # Autorise l'envoi de messages

    # Appliquer les permissions spécifiques à l'utilisateur qui a déclenché la commande
    members = ctx.guild.members
    delete_message = None  # Référence pour le message à supprimer

    for i, member in enumerate(members):
        await channel.set_permissions(member, overwrite=overwrite)
        if delete_message:
            await delete_message.delete()  # Supprimer le dernier message du bot
        delete_message = await ctx.send(f"Accès bloqué à {i} sur {len(members)}")

    await ctx.send(f"Accès bloqué à tous. Authorisation d'accès pour vous en cours...")
    await channel.set_permissions(ctx.author, overwrite=sender)

    # Envoyer un message de confirmation éphémère
    await ctx.send("Le salon privé a été créé, seul vous pouvez y accéder.", ephemeral=True)


@client.command()
async def ping(ctx):
    botLatency = client.latency
    user = ctx.message.author
    await ctx.send(f"La latence du bot est {truncate(botLatency, 5)}ms")
    consoleLog(log.info, f"@{user.name} Executed command /ping.")


@client.command()
async def testmenu(ctx):
    options = []

    # Vérifie si le contexte a une guilde associée
    if ctx.guild:
        server = ctx.guild
        for member in server.members:
            if not member.bot and member.status is not discord.Status.offline:

                emojis = {
                    discord.Status.online: "🟢",
                    discord.Status.idle: "🌙",
                    discord.Status.do_not_disturb: "⛔",
                    discord.Status.offline: "⚪"
                }

                current_date = datetime.datetime.now(member.joined_at.tzinfo)

                time_delta = current_date - member.joined_at

                days = time_delta.days
                hours, remainder = divmod(time_delta.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)

                time_since_join = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds ago."
                options.append(discord.SelectOption(label=member.name, emoji=emojis.get(member.status),
                                                    description=f"Joined {time_since_join}"))

                # Limite le nombre de membres à 25
                if len(options) >= 25:
                    break

        select = Select(
            placeholder=f"Select players for this game. There are {len(options)} available.",
            options=options
        )
        view = View()
        view.add_item(select)
        await ctx.send("Hehe", view=view)
    else:
        await ctx.send("Cette commande ne peut être utilisée que sur un serveur, pas en message privé.")


@client.command()
async def lobbys(ctx):

    GM = GameManager.GameManager()

    user = ctx.message.author

    Lobbys = ""
    for _ in GM.ViewGames():
        Lobbys = Lobbys + f"- {_}\n"


    await ctx.send(f"""There are {len(GM.ViewGames())} active lobbys.
                    {Lobbys}""")

    consoleLog(log.info, f"@{user.name} Executed command /ping.")


client.run("Some token")

# ======================================================================================================================
#                             This file is a part of TechnoSpirit's LunaFur bot. If you want
#                             to modify it, or do your own version, but you are taking parts
#                             of this version, please leave this text at the end of the file
#                                                           ---
#                             Thank you for using LunaFur and I hope it satisfied your needs
#
# ======================================================================================================================
