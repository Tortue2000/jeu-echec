


class echecError(Exception):
    def __str__(self):
        if self.args and self.args[0]:
            return f'echecError: «{self.args[0]}»'
        return 'echecError'    

"""
Voici la classe echec. Dans cette classe, je vais définir les différentes méthodes permettant de modifier l'état du jeu.
"""

class echec():
    def __init__(self):
        self.__partie = {"joueur1": {"pion": [[], [], [], [], [], [], [], []], "tour": [[], []],
         "cavalier": [[], []], "fou": [[], []], "reine": [], "roi": []}, 
        
        "joueur2": {"pion": [[], [], [], [], [], [], [], []], "tour": [[], []],
         "cavalier": [[], []], "fou": [[], []], "reine": [], "roi": []}
        }


    def deplacement(self):
        raise echecError("Il n'y a pas de méthode valide d'implanter pour exécuter ce déplacement")

    

    def afficher_damier(self):
        pass

    def etat_partie(self):
        return self.__partie

    