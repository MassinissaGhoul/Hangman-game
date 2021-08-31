#############################
## Pendu fait par TenixOue ##
#############################




import random  #J'importe les commande de la library random
from fonction import *  #je recupere mes fonctions



chemin=input("Entrez ou se trouve le fichier contenant les mots ")#recupere la liste contenant les mots

if chemin == "": # si l'utilisateur n'entre pas de fichier je prend mots.txt comme fichier de base
    chemin = "mots.txt"





utiliser =[] #tableau qui contiendra les lettre deja entrer pas l'utilisateur
lc =liste(chemin) #appel la Fonction liste avec le chemin donner par l'utilisateur et l'initialise sur la variable lc
mots = random.choice(lc)  #recupere un mot aléatoirement
mots = mots.upper() #met le mot en majuscule
reponse =underscore(mots) #crée une variable contenant mon mot sous forme d'underscore

detail2=list(mots) #met mon mot sous forme de tableau
underscore_liste=list(reponse) # met mon mot en underscore sous forme de tableau

data={"player":input("entre votre nom: ") , "score": 0,"Nombre d'erreur": 0 } #dictionnaire avec les données que j'utilise



print(underscore_liste)

while "_" in underscore_liste and data["Nombre d'erreur"] < 7:    #boucle du jeu qui permet l'arret ou le lancement du jeu
    proposition=entrer() #proposition devient egale a la lettre que l'utilsateur entre grace a la fonction entrer()
    tqt=list(proposition)#tqt

    if verification(proposition,mots) == True and proposition not in utiliser :  #verifie si la proposition est dans le mot et qu'elle n'a jamais etait entrer
        print("Bravo Tu a trouver une lettre")
        data["score"] = data["score"] + 12
        utiliser= utiliser + tqt #ajoute les lettre proposer par l'utilisateur dans un tableau
        for i in range(len(detail2)): #affiche les underscore avec la ou les lettre trouver
            if proposition == detail2[i]:
                underscore_liste[i]=proposition
        print(underscore_liste)

    elif proposition  in utiliser : #verifie si la  proposition a deja etait proposer
        utiliser= utiliser + tqt
        data["score"]= data["score"] - 5
        print("ta la mémoire courte ? tu la déja mise ")
    else: #s'execute si les verification au dessus ne passe pas , donc la proposition  est fausse
        utiliser= utiliser + tqt
        data["score"] = data["score"] - 12
        print("Fait un effort mec , c'est faux")

        data["Nombre d'erreur"] = data["Nombre d'erreur"] +1

        print(dessinPendu(data["Nombre d'erreur"]-1))
if data["Nombre d'erreur"] <7: #boucle de fin de jeu dans ce cas l'utilisateur a gagner
    print(data["player"]  , "tu es trop chaud bg, tu serait pas un dictionnaire ?", data["score"] ,"tu a un bon score ")


else: #joli shrek implementer par moi qui s'affiche si l'utilisateur a perdu
    print("bon bah",data["player"] , "tu a perdu , je m'attendais a mieux ", "ton score est de ", data["score"],  "c'est une catastrophe , voila un shrek pour te consoler " )
    print("⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ ")
    print("⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ ")
    print("⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ ")
    print("⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉")


