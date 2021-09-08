### IMPORT
import time
### FROM
from time import sleep, time
from tqdm import tqdm

### PSEUDO ASK
player = input("Qu'elle est votre pseudo ? > ")

### DONNES

healt = 20
wallet = 50

couteau = 50 # Degat 5
sword = 100 # Degat 10
pistole = 150 # Degat 20


blob_niv1 = 10 # Degat 5

couteau_buy = False
sword_buy = False
pistole_buy = False

fight_blob_niv1 = False

### START
print("Bienvenue",player," Vous avez ",wallet,"$ Votre nombre de vie ",healt,"pv")

### DEF
def walk():
    print("Vous etes entrain de vous balader !")
    for i in tqdm(range(10)):
        sleep(0.5) #base 0.5
        
        
def walk2():
    print("Vous etes entrain de le voir !")
    for i in tqdm(range(10)):
        sleep(2) #base 2
        
def fight_blob(blob_niv1, healt, wallet):
    while True:
        if blob_niv1 == 0:
            break
        print("Blob Niv : 1\nPv : 10")
        print("Vous attacker !")
        sleep(1)
        if couteau_buy == True:
            blob_niv1 -= 5
        if sword_buy == True:
            blob_niv1 -= 10
        if pistole_buy == True:
            blob_niv1 -= 15
        print("Pv Blob: ",blob_niv1)  
        print("Il vous attack !")
        sleep(1)
        healt -= 5
        print("Vos Pv: ",healt)
    print(blob_niv1)
    print('Vous avez gagnez !')
    print("Vous gagnez 20$")
    wallet += 20
    healt == 20
    print("Vous avez {}$".format(wallet))

    
          
        
walk()

ask_weapon_png = input("Vous avez vu un vendeur d'arme vous voulez le voir ? (Oui/Non)")
if ask_weapon_png == "Oui":
    walk()
else:
    pass

    ### ASK WEAPON START
ask_weapon = input("Vous voulez achetez une arme vous avez {}$ ? (Oui/Non)".format(wallet))

### SHOP
if ask_weapon == "Oui":
    list_weapon = input("Voici la liste des armes ! \n1: Couteau\n2: Epee\n3: Pistolet\n> ")
    if list_weapon == "Couteau":
        if wallet == 0:
            print("Vous n'avez pas 50 $, votre argent {}$".format(wallet))
        else:
            wallet -= couteau
            print("Vous avez un couteau !")
            print("Il vous reste {}".format(wallet))
            couteau_buy = True
            print(couteau_buy)
    if list_weapon == "Epee":
        if wallet == 100:
            print("Vous n'avez pas 100 $, votre argent {}$".format(wallet))
        else:
            wallet -= sword
            print("Vous avez une epee !")
            print("Il vous reste {}".format(wallet))
            sword_buy= True
            print(sword_buy)
    if list_weapon == "Pistolet":
        if wallet == 150:
            print("Vous n'avez pas 150 $, votre argent {}$".format(wallet))
        else:
            wallet -= pistole    
            print("Vous avez un pistolet !")
            print("Il vous reste {}".format(wallet))
            pistole_buy = True
            print(pistole_buy)
    else:
        pass



ask_walk_distance = input("Au loin vous voyez un monstre vous voulez l'attacker ? (Oui/Non)")
if ask_walk_distance == "Oui":
    walk2()
    fight_blob(blob_niv1, healt, wallet)
else:
    print("Fin de la beta !")
    




