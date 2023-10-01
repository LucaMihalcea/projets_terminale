#mini projet defi 1


def check_chiffres_in_nombre(chiffres: list, nombre: int)-> bool:
    """
    Test si tout les chiffres d'une liste sont presents dans un nombre
    ------
    input :
    chiffres : list
    nombre : int
    ------
    output : bool 
    """
    for i in chiffres: #parcours la liste
        if i not in list(str(nombre)): #teste si l'element de la liste donc le chiffre n'est pas dans le nombre
            return False #retoune False si il n'y est pas
    return True #retourne True si apres avoir teste tout les chiffres de la liste aucun ne manque dans le nombre

def mdp()-> tuple:
    """
    Retourne les trois prochains mots de passes de la cabine du mini projet
    ------
    input : None
    ------
    output : tuple
    """
    tpl = () #initialisation d'un tuple vide
    c_1 = 64224 #initialisation du mot de passe courant pour tester ceux d'apres
    chiffres_carre = ['1','2','4','6','7'] #initialisation de la liste de chiffres que le mot de passe au carre doit contenir
    while len(tpl) < 3: # tant qu'il n'y a pas tois mots de passe on continue a chercher
        c_1 += 1 #on cherche pour l'entier suivant 
        if check_chiffres_in_nombre(chiffres_carre, c_1**2): #on teste si tout les chiffres de la liste sont dans le potentiel mot de passe au carre 
            tpl += c_1, #si tout les chiffres y sont on l'ajoute au tuple contenant les mots de passes 
    return tpl #une fois les trois mots de passes trouves on retoune le tuple les contenant

print("les trois prochains mots de passes seront :", mdp()) #affiche les trois prochains mots de passes 
