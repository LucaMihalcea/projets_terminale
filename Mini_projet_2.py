from random import randint

class Piece:
    def __init__(self, valeur: int, masse: int):
        self.__valeur = valeur 
        self.__masse = masse
    
    def getMasse(self):
        """
        Permet d'obtenir la masse d'une piece 
        Output : Int
        """
        return self.__masse
    
    def getValeur(self):
        """
        Permet d'obtenir la valeur d'une piece 
        Output : Int
        """
        return self.__valeur
    
    def estFausse(self):
        """
        Permet de tester si une pièce est bien fausse (Utile dans les jeux de tests)
        Output : bool
        """
        return self.__masse == 9
    
    def __repr__(self):
        """
        Permet d'afficher un objet de la class Piece
        Output : str
        """
        return "(" + str(self.__valeur) + "," + str(self.__masse) + ")"
    
    def __eq__(self, piece2):
        """
        Permet de verifier l'égalité entre deux Piece (Utile dans les jeux de tests)
        Input : Piece
        Output : bool
        """
        assert type(piece2) == Piece
        return self.__valeur == piece2.getValeur() and self.__masse == piece2.getMasse()

#jeu de test de la class piece
piece_test_1 = Piece(3,9)
piece_test_2 = Piece(12,10)
piece_test_3 = Piece(7,9)
piece_test_4 = Piece(4,9)

assert piece_test_1.getMasse() == 9
assert piece_test_1.getValeur() == 3
assert piece_test_1.estFausse() == True

assert piece_test_2.getMasse() == 10
assert piece_test_2.getValeur() == 12
assert piece_test_2.estFausse() == False

assert piece_test_3.getMasse() == 9
assert piece_test_3.getValeur() == 7
assert piece_test_3.estFausse() == True

assert piece_test_4.getMasse() == 9
assert piece_test_4.getValeur() == 4
assert piece_test_4.estFausse() == True


class Tas_de_pieces:
    def __init__(self):
        self.__tas = []
    
    def ajouter(self, pieces : Piece):
        """
        Permet d'ajouter une piece au tas
        Input : Piece
        """
        assert type(pieces) == Piece 
        self.__tas.append(pieces)
    
    def est_vide(self):
        """
        Verifie si une liste est vide 
        Output : bool
        """
        if self.__tas == []:
            return True 
        return False 
        
    def piocher(self):
        """
        Permet de piocher une piece au hasard
        Output : Piece
        """
        #preconditions
        assert not self.est_vide()

        idx_piece = randint(0, (len(self.__tas) - 1))
        piece = self.__tas[idx_piece]
        self.__tas.pop(idx_piece)
        return piece
    
    def diviser(self) -> tuple:
        """
        Divise le tas aléatoirement en deux autres tas
        Output : tuple
        """
        #preconditions
        assert not self.est_vide()

        c = 0 
        tas1 = Tas_de_pieces()
        tas2 = Tas_de_pieces()
        while not self.est_vide():
            if c%2 == 0:
                tas1.ajouter(self.piocher())
                c += 1
            else:
                tas2.ajouter(self.piocher())
                c += 1

        #postconditions:
        assert 0 <= tas1.taille() - tas2.taille() <= 1
        return tas1, tas2

    def peser(self):
        """
        Donne la masse totale du tas
        Output : int
        """
        if self.est_vide():
            return 0
        somme = 0
        for piece in self.__tas:
            somme += piece.getMasse()
        
        #postconditions
        assert somme > 0
        return somme
    
    def taille(self):
        """
        Donne la taille du tas
        Output : int
        """
        return len(self.__tas)
    
    def estCorrompu(self):
        """
        Verifie si un tas est corrompu
        Output : bool
        """
        masse = self.peser()
        return masse % 10 == 9
    
    def copy(self):
        """
        Crée une copie du tas permettant de ne pas le modifier mais de modifier la copie
        Output : Tas_de_pieces
        """
        tas_copie = Tas_de_pieces()
        for i in self.__tas:
            tas_copie.ajouter(i)
        return tas_copie
    
    def __repr__(self):
        """
        Permet l'affichage du tas 
        Output : str
        """    
        return "Le tas est : " + str(self.__tas)


def valeur_totale(tas : Tas_de_pieces) -> int:
    """
    Retourne la valeure totale d'un tas de piece 
    """
    tas_copie = tas.copy()
    if tas_copie.est_vide():
        return 0
    piece = tas_copie.piocher()
    return piece.getValeur() + valeur_totale(tas_copie)

def  trouver_fausse_piece(tas : Tas_de_pieces) -> Piece:
    """
    Trouve une fuasse piece dans un tas corrompu
    """
    tas_copie = tas.copy()
    if tas_copie.estCorrompu(): #teste si le tas est corrompu
        if tas_copie.taille() == 1:
            fausse_piece = tas_copie.piocher()
            assert fausse_piece.estFausse()
            return fausse_piece
        else :
            division = tas_copie.diviser()
            tas1 = division[0]
            tas2 = division[1]
            if tas1.estCorrompu():
                return trouver_fausse_piece(tas1)
            else: 
                return trouver_fausse_piece(tas2)

#jeu de test classe Tas_de_pieces et fonctions annexes
tas_test_1 = Tas_de_pieces()
tas_test_1.ajouter(Piece(2,10))
tas_test_1.ajouter(Piece(3,10))
tas_test_1.ajouter(Piece(2,10))
tas_test_1.ajouter(Piece(3,9))
tas_test_1.ajouter(Piece(7,10))
tas_test_1.ajouter(Piece(6,10))
tas_test_1.ajouter(Piece(2,10))

tas_test_2 = Tas_de_pieces()
tas_test_2.ajouter(Piece(1,9))
tas_test_2.ajouter(Piece(2,10))
tas_test_2.ajouter(Piece(4,10))
tas_test_2.ajouter(Piece(8,10))
tas_test_2.ajouter(Piece(16,10))
tas_test_2.ajouter(Piece(32,10))
tas_test_2.ajouter(Piece(64,10))
tas_test_2.ajouter(Piece(128,10))

tas_test_3 = Tas_de_pieces()

tas_test_4 = Tas_de_pieces()
tas_test_4.ajouter(Piece(12,10))
tas_test_4.ajouter(Piece(3,10))
tas_test_4.ajouter(Piece(2,10))
tas_test_4.ajouter(Piece(3,10))
tas_test_4.ajouter(Piece(27,10))
tas_test_4.ajouter(Piece(16,10))
tas_test_4.ajouter(Piece(2,10))

assert tas_test_1.est_vide() is False
assert tas_test_1.peser() == 69
assert tas_test_1.taille() == 7
assert tas_test_1.estCorrompu() is True
assert valeur_totale(tas_test_1) == 25
assert trouver_fausse_piece(tas_test_1) == Piece(3,9)

assert tas_test_2.est_vide() is False
assert tas_test_2.peser() == 79
assert tas_test_2.taille() == 8
assert tas_test_2.estCorrompu() is True
assert valeur_totale(tas_test_2) == 255
assert trouver_fausse_piece(tas_test_2) == Piece(1,9)

assert tas_test_3.est_vide() is True
assert tas_test_3.peser() == 0
assert tas_test_3.taille() == 0
assert tas_test_3.estCorrompu() is False
assert valeur_totale(tas_test_3) == 0

assert tas_test_4.est_vide() is False
assert tas_test_4.peser() == 70
assert tas_test_4.taille() == 7
assert tas_test_4.estCorrompu() is False
assert valeur_totale(tas_test_4) == 65

#Simple affichage pour les methodes aleatoires ne pouvant pas etre testees 
print("tas_test_1 :")
print("La piece piochee est : " + str(tas_test_1.piocher()))
print(tas_test_1)
print(tas_test_1.diviser())
print(tas_test_1, "\n")

print("tas_test_2 :")
print("La piece piochee est : " + str(tas_test_2.piocher()))
print(tas_test_2)
print(tas_test_2.diviser())
print(tas_test_2, "\n")

print("tas_test_4 :")
print("La piece piochee est : " + str(tas_test_4.piocher()))
print(tas_test_4)
print(tas_test_4.diviser())
print(tas_test_4, "\n")