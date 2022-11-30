from modele.Score import Score


class Player:
    ID = 1
    def __init__(self,username):
        self.id = Player.ID
        self.username = username
        self.nombrePartie = 0
        self.score = Score(0,0,0)
        Player.ID+=1