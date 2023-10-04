#mini projet defi 1

def number_to_digits(number: int) -> set:
    """
    Prend en entree un entier et retourne les chiffres qui le composentsous la forme d'un set
    ------
    input :
    number : int
    ------
    output :
    digits : set
    ------
    complexite : O(n) avec n le nombre de chiffres de number
    """

    #precondition
    assert type(number) == int

    #code
    digits = set() #initialisation d'une variable digits en set vide
    m = number #copie de number en "m" pour ne pas modifier l'input
    if m == 0: #gere le cas ou m est nul
        return {0}
    while m != 0:
        digits.add(m%10) #on ajoute a digits le reste de la division euclidienne de m par 10 soit l'unite de m
        m = m//10

    #postcondition
    assert type(digits) == set

    return digits


#jeu de test number_to_digits
assert number_to_digits(1234) == {1,2,3,4}
assert number_to_digits(1) == {1}
assert number_to_digits(45673235) == {4,5,6,7,3,2,}


def check_digits_in_number(digits: set, number: int)-> bool:
    """
    Test si tout les chiffres d'un set sont presents dans un nombre et si ce sont les seuls chiffres de ce nombre
    ------
    input :
    digits : set
    number : int
    ------
    output : bool
    ------
    complexite : O(n) avec n le nombre de chiffre de number
    """

    #preconditions :
    assert type(digits) == set and type(number) == int

    #code
    return digits == number_to_digits(number)


#jeu de test check_digits_in_number
assert check_digits_in_number({1,2,3,4}, 1234) == True
assert check_digits_in_number({1,2,3,4}, 1432) == True
assert check_digits_in_number({1,2,3,4}, 14325) == False


def passwords()-> tuple:
    """
    Retourne les trois prochains mots de passes de la cabine du mini projet
    ------
    input : Aucun
    ------
    output : tuple
    """
    tpl = () #initialisation d'un tuple vide
    c_1 = 64224 #initialisation du mot de passe courant pour tester ceux d'apres
    chiffres_carre = {1,2,4,6,7} #initialisation de la liste de chiffres que le mot de passe au carre doit contenir
    while len(tpl) < 3: # tant qu'il n'y a pas tois mots de passe on continue a chercher
        c_1 += 1 #on cherche pour l'entier suivant
        if check_digits_in_number(chiffres_carre, c_1**2): #on teste si tout les chiffres de la liste sont dans le potentiel mot de passe au carre
            tpl += c_1, #si tout les chiffres y sont on l'ajoute au tuple contenant les mots de passes
    #postcondition
    assert type(tpl) == tuple
    return tpl #une fois les trois mots de passes trouves on retoune le tuple les contenant


print("les trois prochains mots de passes seront :", passwords())