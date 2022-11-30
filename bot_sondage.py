import discord
from discord.ext import commands
from environ import *
from modele.Sondage import Sondage

intents = discord.Intents.all()
bot = commands.Bot(command_prefix= "!" , intents=intents)
sondage = Sondage()

@bot.command(name="lancerSondage")
async def lancerSondage(ctx, Question, choix1, choix2, choix3, choix4):
    '''
    Exemple d'utilisation !lancerSondage "Quelle est votre couleur préférée" bleu blanc rouge "Aucune parmi la liste"
    Pour lancer un sondage, utiliser la commande !lancerSondage question choix1 choix2 choix3 choix4
    Mettre entre " " les questions ou choix qui possède plus d'un mot.
    Arguments
    ---------
        Question : String
        choix1 : String
        Choix2 : String
        Choix3 : String
        Choix4 : String
    '''
    if sondage.statut:
        await ctx.send("`Il y a deja un sondage en cours ... Utiliser d'abord la commande !terminerSondage ou !kill`")
    else:
        choix = [choix1, choix2, choix3, choix4]
        sondage.newSondage(Question, choix)
        msg = sondage.statutSondage()
        await ctx.send(msg)

@bot.command(name ="kill")
async def killsondage(ctx):
    '''
    Exemple d'utilisation !killsondage
    Supprime le sondage, indispensable pour en creer un nouveau.
    Il est aussi possible de terminer un sondage avec la commande !terminerSondage pour avoir en plus le résultat
    '''
    if sondage.statut:
        sondage.resetSondage()
        await ctx.send("`Sondage reinitialisée`")
    else:
        await ctx.send("`Pas de sondage a kill`")

@bot.command(name = "repondre") 
async def repondre(ctx, reponse):
    '''
    Exemple d'utilisation : !repondre 2 
    Rajoute un vote, choisir un nombre parmi 1, 2, 3 ou 4
    '''
    rep=int(reponse)
    choises = [1,2,3,4]
    if rep not in choises:
        await ctx.send("`La réponse doit être 1, 2, 3 ou 4`")
    else:
        msg = sondage.ajouterVote(rep)
        await ctx.send(msg)

@bot.command(name = "statut")
async def statut(ctx):
    '''
    Exemple d'utilisation : !statut
    Affiche l'etat des votes actuel pour le sondage
    '''
    msg = sondage.statutSondage()
    await  ctx.send(msg)

@bot.command(name = "terminerSondage")
async def terminerSondage(ctx):
    '''
    Exemple d'utilisation : !terminerSondage
    Terminer le sondage et affiche le resultat s'il n'y a pas d'égalité.
    '''
    if sondage.statut:
        msg = sondage.resultsSondage()
        if 'question' in msg:
            await ctx.send(msg)
            sondage.resetSondage()
        else:
            await ctx.send(msg)
    else:
        await ctx.send("`Pas de sondage en cours`")
            




bot.run(BOT_KEY)