import discord
from discord.ext import commands
from environ import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix= "!" , intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} est connecté')
    # channel = bot.get_channel(1029289071840874497)
    # await channel.send("coucou")


def verifyListNotOnString(mots: list[str], message : str)-> bool:
    for mot in mots:
        if mot.upper() in message.upper():
            return True
    return False

def allVariationWord(mot : str)->list:
    origin = mot.upper()
    temp_mot = mot.upper()
    c_variation = ['C', 'S', '$']
    a_variation = ['A','4','@']
    e_variation = ['E','3', '€']
    o_variation = ['O', 'ø', '0']
    result = []
    for i in a_variation:
        compteur1 = 0
        compteur2 = 0
        compteur3 = 0
        # compteur4 = 0
        for j in e_variation:
            modif = False
            temp_mot = list(origin)
            for lettre in list(origin):  
                if lettre == 'C':
                    index_c = temp_mot.index('C')
                    temp_mot[index_c] = c_variation[compteur4]
                    modif = True
                    compteur4+=1
                if lettre == 'A':
                    index_a = temp_mot.index('A')
                    temp_mot[index_a] = a_variation[compteur1]
                    compteur1+=1
                    modif = True
                if lettre == 'E':
                    index_e = temp_mot.index('E')
                    temp_mot[index_e] = e_variation[compteur2]
                    modif = True
                    compteur2+=1
                if lettre == 'O':
                    index_o = temp_mot.index('O')
                    temp_mot[index_o] = o_variation[compteur3]
                    modif = True
                    compteur3+=1 
            if modif:
                result.append(temp_mot)
    result2 = []
    for res in result:
        res = "".join(res)
        result2.append(res)
    result2 = list(map(lambda x:''.join(char for char in x if char.isalnum()), result2))
    return result2
                
forbbidenWords = allVariationWord('chauve') + allVariationWord('chove') + allVariationWord('chauv') + allVariationWord('chov')
print(forbbidenWords)

@bot.event
async def on_message(message):
    print(message.content)
    print(message.author)
    modify_message = message.content.upper().split()
    modify_message = list(map(lambda x:''.join(char for char in x if char.isalnum()), modify_message))
    modify_message = ' '.join(modify_message)
    if message.author != bot.user:
        if (verifyListNotOnString(forbbidenWords,modify_message)):
            await message.delete()
            await message.channel.send(f'{message.author.mention} Ce mot est interdit !!')
            

bot.run(BOT_KEY)
