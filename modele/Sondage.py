
class Sondage:
    def __init__(self, question="", choix=["","","",""], results = [0,0,0,0],statut=False):
        self.question = question
        self.choix = choix
        self.statut = statut
        self.results = results

    def ajouterVote(self, num):
        self.results[num-1] += 1
        return f"`1 vote ajouté pour {self.choix[num-1]}`"

    def resetSondage(self):
        self.question = ""
        self.choix = ["","","",""]
        self.statut = False
        self.results = [0,0,0,0]
    
    def newSondage(self, question, choix):
        self.question = question
        self.choix = choix
        self.statut = True
        self.results = [0,0,0,0]

    def statutSondage(self):
        if self.statut:
            return f"```\n(sondage en cours :) \n Question : {self.question} \n Choix : \n - 1) {self.choix[0]} --> {self.results[0]} votes\n - 2) {self.choix[1]} --> {self.results[1]} votes\n - 3) {self.choix[2]} --> {self.results[2]} votes\n - 4) {self.choix[3]} --> {self.results[0]} votes```"
        else:
            return f"`Pas de sondage en cours`"

    def startSondage(self):
        if self.statut:
            return "`Le sondage a déhà été lancé`"
        else:
            self.statut = True
            return "`Un sondage a été lancé`"
    
    def resultsSondage(self):
        if sorted(self.results)[2] == sorted(self.results)[3]:
            return "`Le sondage ne peut pas se terminer en cas d'égalité`"
        else:
            nombreVote = max(self.results)
            indx=self.results.index(nombreVote)
            gagnant = self.choix[indx]
            return f"```\n Résultat du sondage pour la question \"{self.question}\" : \n \"{gagnant}\" avec un total de {nombreVote} ```" 

        
