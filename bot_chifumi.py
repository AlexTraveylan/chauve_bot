import discord
from discord.ext import commands
from environ import *
import random
from modele.Player import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix= "!" , intents=intents)

listChoix = ["pierre", "feuille", "ciseaux"]
listJoueur = []

@bot.command(name="score")
async def scoreJoueur(ctx):
    if ctx.author in list(map(lambda x:x.username,listJoueur)):
        for i in listJoueur:
            if i.username == ctx.author:
                player = i 
        
        msg = f"```\nScore de {player.username} :\n Win : {player.score.win}\n Lose : {player.score.lose}\n Egalité : {player.score.tie}```"

    else:msg="`Tu n'as pas encore joué contre moi.`"
    await ctx.send(msg)


@bot.command(name="chifumi")
async def chifumi(ctx, choix):
    if ctx.author in list(map(lambda x:x.username,listJoueur)):
        for i in listJoueur:
            if i.username == ctx.author:
                player = i 
    else:
        player = Player(ctx.author)
        listJoueur.append(player)
            
    if choix in listChoix:
        alea = random.randint(1,3)
        result = ""
        choixServeur=""
        player.nombrePartie+=1

        if alea==1:
            result="J'ai perdu !"
            choixServeur = listChoix[(listChoix.index(choix)+2)%3]
            player.score.win +=1

        elif alea ==2:
            result="J'ai gagné !"
            choixServeur = listChoix[(listChoix.index(choix)+1)%3]
            player.score.lose +=1

        else:
            result ="Match nul !"
            choixServeur = choix
            player.score.tie +=1

        msg = f"`{result} Tu as choisi {choix} et moi {choixServeur}`"

    else:
        msg="`pierre, feuille ou ciseaux sont les seuls choix possibles`"
    await ctx.send(msg)








bot.run(BOT_KEY)