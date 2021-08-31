#############################
## Pendu fait par TenixOue ##
#############################




def dessinPendu(nb): #Fonction qui dessine le pendu
    tab=[
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[nb]


#fonction qui met des underscore a la place du mots 
def underscore(r):
    return "".join("_" for _ in range(len(r)))

def liste(fichier):#Fonction qui permet de de recuperer et stocker la liste de mot souhaiter , enleve aussi les retour a la ligne (\n)
        lc=[]
        ls=open(fichier,"r")
        premier=ls.readline()

        while premier!="":
            premier=premier.rstrip("\n")
            lc.append(premier)
            premier=ls.readline()

        return (lc)


def entrer():#Fonction recuperant la lettre de l'utilisateur
    lettre = input("Entrez une lettre : ")
    if len( lettre ) > 1:
        return entrer()
    else:
        return lettre.upper()



#Fonction qui verifie si la lettre donner est dans le mot
def verification(prop,t):
    detail=list(t)

    return prop in detail  

def WordPresentation(underscore): #fonction qui enleve les truc moche de underscore_liste('' et [] )  
    
    pass