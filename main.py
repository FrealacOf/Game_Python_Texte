### IMPORT
import time
### FROM
from time import sleep, time
from tqdm import tqdm
import random

### PSEUDO ASK
player = input("Qu'elle est votre pseudo ? > ")

### DONNES

### ### XP +
force = 0
resistance = 0


healt = 20
wallet = 100

couteau = 50 # Degat 5
sword = 100 # Degat 10
pistole = 150 # Degat 20

xp = 0

blob_niv1 = 10 # Degat 5
sorcier_niv1 = 20 # Degat 10


couteau_buy = False
sword_buy = False
pistole_buy = False

fight_blob_niv1 = False

### START
print("Bienvenue",player," Vous avez ",wallet,"$ Votre nombre de vie ",healt,"pv")

### DEF
### SHOP 
def list_weapon():
    global wallet
    global couteau_buy
    global sword_buy
    global pistole_buy
    list_weapon = input("Voici la liste des armes ! \n1: Couteau\n2: Epee\n3: Pistolet\n> ")
    if list_weapon == "Couteau":
        if wallet == 0:
            print("Vous n'avez pas 50 $, votre argent {}$".format(wallet))
        if wallet > 50:
            wallet -= couteau
            print("Vous avez un couteau !")
            print("Il vous reste {}".format(wallet))
            couteau_buy=True
            print(couteau_buy)
    if list_weapon == "Epee":
        if wallet == 100:
            print("Vous n'avez pas 100 $, votre argent {}$".format(wallet))
        if wallet > 100:
            wallet -= sword
            print("Vous avez une epee !")
            print("Il vous reste {}".format(wallet))
            sword_buy=True
            print(sword_buy)
    if list_weapon == "Pistolet":
        if wallet == 150:
            print("Vous n'avez pas 150 $, votre argent {}$".format(wallet))
        if wallet > 150:
            wallet -= pistole    
            print("Vous avez un pistolet !")
            print("Il vous reste {}".format(wallet))
            pistole_buy=True
            print(pistole_buy)  
            
### WALK BAR           
def walk():
    print("Vous etes entrain de vous balader !")
    for i in tqdm(range(10)):
        sleep(0.1) #base 0.5
        
        
def walk2():
    print("Vous etes entrain de le voir !")
    for i in tqdm(range(10)):
        sleep(0.1) #base 1
### MOBS     
def fight_blob(blob_niv1, healt):
    global xp
    global wallet
    global couteau_buy
    global sword_buy
    global pistole_buy
    ask_attack_blob = input("Vous voulez l'attacker ? (Oui/Non)\nSTATS\nPv : 10\nDegat : 5\n> ")
    if ask_attack_blob == "Oui":
        while True:
            if blob_niv1 == 0:
                print(blob_niv1)
                print('Vous avez gagnez !')
                xp += 5 
                wallet += 20
                healt = 20
                print("Vous gagnez 20$ + ",xp,"XP TOTAL : ",wallet,"$")
                ask_weapon_buy2 = input("Vous voulez allez voir le shop ? (Oui/Non)")
                if ask_weapon_buy2 == "Oui":
                    list_weapon()
                else:
                    pass
                break
            if healt == 0:
                print("Vos Pv : ",healt)
                print("Vous avez perdu !")
                sleep(2)
                break
            if couteau_buy == False:
                print("Vous n'avez pas d'arme !")
                list_weapon(wallet, couteau_buy, sword_buy, pistole_buy)
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
    else:
        ask_weapon_buy3 = input("Vous voulez voir le shop ? (Oui/Non)")
        if ask_weapon_buy3 == "Oui":
            list_weapon()
        if ask_weapon_buy3 == "Non":
            pass
        ask_walk_distance = input("Au loin vous voyez un monstre vous voulez l'attacker ? (Oui/Non)")
        if ask_walk_distance == "Oui":
            walk2()
            if random.randint(0, 1) == 0:
                print("Vous avez trouvez un BLOB")
                sleep(1)
                fight_blob(blob_niv1, healt)
            else:
                print("Vous avez trouver un SORCIER")
                sleep(1)
                fight_sorcier(sorcier_niv1, healt)

    
def fight_sorcier(sorcier_niv1, healt):
    global xp
    global wallet
    global couteau_buy
    global sword_buy
    global pistole_buy
    ask_attack_sorcier = input("Vous voulez l'attacker ? (Oui/Non)\nSTATS\nPv : 20\nDegat : 10\n> ")
    if ask_attack_sorcier == "Oui":
        while True:
            if sorcier_niv1 == 0:
                print(sorcier_niv1)
                print('Vous avez gagnez !')
                xp += 10
                wallet += 40
                healt = 20
                print("Vous gagnez 40$ + ",xp,"XP TOTAL : ",wallet,"$")
                ask_weapon_buy2 = input("Vous voulez allez voir le shop ? (Oui/Non)")
                if ask_weapon_buy2 == "Oui":
                    list_weapon()
                else:
                    pass
                break
            if healt == 0:
                print("> Vos Pv : ",healt)
                print("Vous avez perdu !")
                sleep(2)
                break
            if couteau_buy == False:
                print("Vous n'avez pas d'arme !")
                list_weapon(wallet, couteau_buy, sword_buy, pistole_buy)
                break
            print("Sorcier Niv : 1\nPv : 10")
            print("Vous attacker !")
            sleep(1)
            if couteau_buy == True:
                sorcier_niv1 -= 5
            if sword_buy == True:
                sorcier_niv1 -= 10
            if pistole_buy == True:
                sorcier_niv1 -= 15
            print("Pv Sorcier: ",sorcier_niv1)  
            print("Il vous attack !")
            sleep(1)
            healt -= 10
            print("Vos Pv: ",healt)
    else:
        ask_weapon_buy3 = input("Vous voulez voir le shop ? (Oui/Non)")
        if ask_weapon_buy3 == "Oui":
            list_weapon()
        if ask_weapon_buy3 == "Non":
            pass
        ask_walk_distance = input("Au loin vous voyez un monstre vous voulez l'attacker ? (Oui/Non)")
        if ask_walk_distance == "Oui":
            walk2()
            if random.randint(0, 1) == 0:
                print("Vous avez trouvez un BLOB")
                sleep(1)
                fight_blob(blob_niv1, healt)
            else:
                print("Vous avez trouver un SORCIER")
                sleep(1)
                fight_sorcier(sorcier_niv1, healt)
walk()

ask_weapon_png = input("Vous avez vu un vendeur d'arme vous voulez le voir ? (Oui/Non)")
if ask_weapon_png == "Oui":
    walk()
    ask_weapon = input("Vous voulez achetez une arme vous avez {}$ ? (Oui/Non)".format(wallet))
    if ask_weapon == "Oui":
        list_weapon()
    if couteau_buy == False:
        print("Vous devez avoir une arme pour avancer")
        list_weapon()
else:
    pass

    ### ASK WEAPON START




ask_walk_distance = input("Au loin vous voyez un monstre vous voulez l'attacker ? (Oui/Non)")
if ask_walk_distance == "Oui":
    walk2()
    if random.randint(0, 1) == 0:
        print("Vous avez trouvez un BLOB")
        sleep(1)
        fight_blob(blob_niv1, healt)
    else:
        print("Vous avez trouver un SORCIER")
        sleep(1)
        fight_sorcier(sorcier_niv1, healt)
else:
    print("Fin de la beta !")
    




