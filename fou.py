from echec import echec


class fou(echec):
    def __init__(self):
        self.__fou1 = ["x", "y"] #Un couple x, y servant à positionner les fous.
        self.__fou2 = ["x", "y"]
    
    def deplacement(self, joueur):
        pass