#mini projet defi 1

def number_to_digits(number: int) -> set:
    """
    Prend en entree un entier naturel et retourne les chiffres qui le composent sous la forme d'un set
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
    assert type(number) == int and number >= 0

    #code
    digits = set() #initialisation d'une variable digits en set vide
    m = number #copie de number en "m" pour ne pas modifier l'input
    if m == 0: #gere le cas ou m est nul
        return {0}
    while m != 0:
        digits.add(m%10) #on ajoute a digits le reste de la division euclidienne de m par 10 soit l'unite de m
        m = m//10

    #postcondition
    assert type(digits) == set and len(digits) > 0

    return digits


#jeu de test number_to_digits
assert number_to_digits(0) == {0}
assert number_to_digits(1234) == {1,2,3,4}
assert number_to_digits(1) == {1}
assert number_to_digits(45673235) == {4,5,6,7,3,2}


def check_digits_in_number(digits: set, number: int)-> bool:
    """
    Verifie si tous les chiffres d'un set sont presents dans un nombre et si ce sont les seuls chiffres de ce nombre
    ------
    input :
    digits : set
    number : int
    ------
    output : bool
    ------
    complexite : O(n) avec n le nombre de chiffres de number
    """

    #preconditions :
    assert type(digits) == set and len(digits) > 0 and type(number) == int

    #code deux sets sont egaux s'ils contiennent les memes elements peu importe l'ordre
    return digits == number_to_digits(number)


#jeu de test check_digits_in_number
assert check_digits_in_number({1,2,3,4}, 1234) == True # cas positif
assert check_digits_in_number({1,2,3,4}, 1432) == True # cas positif l'ordre ne compte pas
assert check_digits_in_number({1,2,3,4}, 14325) == False # cas negatif

#initialisation des constantes
allowed_digits = {1,2,4,6,7} #l'ensemble des chiffres que le mot de passe au carre doit contenir

def passwords(nb_codes: int=3)-> tuple:
    """
    Retourne les trois prochains mots de passes de la cabine du mini projet
    ------
    input :
    nb_codes: int (valeur par defaut 3)
    ------
    output : tuple
    """
    #precondition
    assert type(nb_codes)==int and nb_codes > 0
    
    codes = () #initialisation d'un tuple vide
    candidate = 64224 #initialisation du mot de passe courant pour tester ceux d'apres
    
    while len(codes) < nb_codes: # tant qu'il n'y a pas tois mots de passe on continue a chercher
        candidate += 1 #on cherche pour l'entier suivant
        if check_digits_in_number(allowed_digits, candidate**2): #on teste si tout les chiffres de la liste sont dans le potentiel mot de passe au carre
            codes += candidate, #si tout les chiffres y sont on l'ajoute au tuple contenant les mots de passes

    #postcondition
    assert type(codes) == tuple and len(codes) == nb_codes
    return codes #une fois les trois mots de passes trouves on retoune le tuple les contenant


#verification du programme
actuals = passwords(100)
for code in actuals:
    assert check_digits_in_number(allowed_digits, code**2)
    
print("les trois prochains mots de passes seront :", passwords(3))
