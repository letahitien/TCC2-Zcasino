from random import randrange
from math import ceil

argent = randrange(15, 1500)
print("Bienvenue sur la table à roulette de zCasino \nPour quitter la partie, entre \"0\" \nTu as un portefeuille de", argent, "$")

def portefeuille() :
    print("Portefeuille :", argent, "$")

m = n = False

while True :
    if argent != 0 :
        if m == False :
            try :
                mise = int(input("Combien mises-tu : "))
                if mise == 0 : 
                    print("A très bientôt, tes gains sont de :", argent, "$")
                    break
                assert mise <= argent
                m = True
            except ValueError :
                print("Mise non conforme !")
                continue
            except AssertionError :
                print("Tu ne peux miser plus que ce que tu possède !")
                continue
        if n == False :
            try :
                numero = int(input("Choisis un numéro compris entre 0 et 49 : "))
                if numero == 0 : 
                    print("A très bientôt, tes gains sont de :", argent, "$")
                    break
                assert numero > 0 and numero < 49
                n = True
            except ValueError :
                print("Numéro non conforme !")
                continue
            except AssertionError :
                print("Uniquement un numéro compris entre 0 et 49 !")
                continue
            else :
                m = n = False

        roulette = randrange(50)
        print("Le numéro de la roulette est", roulette)

        couleurRoulette = roulette % 2
        couleurNumero = numero % 2

        if numero == roulette :
            argent += ceil(mise * 3)
            print("Félicitations ! Avec un bon numéro, tu remporte :", ceil(mise * 3), "$")
            portefeuille()
        elif couleurRoulette == 0 and  couleurNumero == 0 :
            argent += ceil(mise * 1.5)
            print("Félicitations ! Avec une couleur noir, tu remporte :", ceil(mise * 1.5), "$")
            portefeuille()
        elif couleurRoulette != 0 and  couleurNumero != 0:
            argent += ceil(mise * 1.5)
            print("Félicitations ! Avec une couleur rouge, tu remporte :", ceil(mise * 1.5), "$")
            portefeuille()
        else : 
            argent -= mise
            print("Tu as perdu !", mise, "$")
            portefeuille()
    else :
        print("Tu as plus d'argent ! Haha...A la prochaine !")
        break
