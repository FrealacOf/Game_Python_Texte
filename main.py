### IMPORT
import time
### FROM
from time import sleep, time
from tqdm import tqdm
import random
import json
from ast import literal_eval

nom_fichier = 'information_player.json'


print("------------------------------------------")
print("   ██████╗ ██╗   ██╗███╗   ██╗██╗██╗  ██╗")
print("  ██╔═══██╗╚██╗ ██╔╝████╗  ██║██║╚██╗██╔╝")
print("  ██║   ██║ ╚████╔╝ ██╔██╗ ██║██║ ╚███╔╝ ")
print("  ██║   ██║  ╚██╔╝  ██║╚██╗██║██║ ██╔██╗ ")
print("  ╚██████╔╝   ██║   ██║ ╚████║██║██╔╝ ██╗")
print("------------------------------------------")
print("")
print("")
### PSEUDO ASK
player = input("Qu'elle est votre pseudo ?\n> ")

### DONNES

### ### XP +
force = 0
resistance = 0


healt = 20
wallet = 100

couteau = 50 # Degat 5
sword = 100 # Degat 10
pistole = 150 # Degat 20

armor_fer = 250 # /0.5
armor_or = 350 # /1
armor_diamant = 500 #/1.5

xp = 0
levels = 0
levels_check = 10

blob_niv1 = 10 # Degat 5
sorcier_niv1 = 20 # Degat 10


armor_fer_buy = False
armor_or_buy = False
armor_diamant_buy = False

couteau_buy = False
sword_buy = False
pistole_buy = False


fight_blob_niv1 = False

### JSON
def ecrire_info():
    global player
    global force
    global resistance
    global healt
    global wallet
    global couteau
    global sword
    global pistole
    global xp
    global levels
    global levels_check
    global couteau_buy
    global sword_buy
    global pistole_buy
    with open(nom_fichier ,'w') as fichier:
        json.dump(str({'name:': player, 'force:': force, 'resistance:': resistance, 'Pv:': healt, 'Money:': wallet, 'Couteau:': couteau, 'Epee:': sword, 'Pistolet': pistole, 'Xp:': xp, 'Levels:': levels, 'Levels_Check:': levels_check, 'Couteau_Buy': couteau_buy, 'Sword_Buy:': sword_buy, 'Gun_Buy:': pistole_buy}), fichier)

### START
print("Bienvenue",player," Vous avez ",wallet,"$ Votre nombre de vie ",healt,"pv")

### DEF
### SHOP 
def list_weapon():
    global wallet
    global couteau_buy
    global sword_buy
    global pistole_buy
    list_weapon = input("Voici la liste des armes ! \n1: Couteau\n2: Epee\n3: Pistolet\n4: Exit\n> ")
    if list_weapon == "Couteau":
        if wallet < 50:
            print("Vous n'avez pas 50 $, votre argent {}$".format(wallet))
        if wallet >= 50:
            wallet -= couteau
            print("Vous avez un couteau !")
            print("Il vous reste {}".format(wallet))
            couteau_buy=True
            print(couteau_buy)
            ecrire_info()
    if list_weapon == "Epee":
        if wallet < 100:
            print("Vous n'avez pas 100 $, votre argent {}$".format(wallet))
        if wallet >= 100:
            wallet -= sword
            print("Vous avez une epee !")
            print("Il vous reste {}".format(wallet))
            sword_buy=True
            print(sword_buy)
            ecrire_info()
    if list_weapon == "Pistolet":
        if wallet < 150:
            print("Vous n'avez pas 150 $, votre argent {}$".format(wallet))
        if wallet >= 150:
            wallet -= pistole    
            print("Vous avez un pistolet !")
            print("Il vous reste {}".format(wallet))
            pistole_buy=True
            print(pistole_buy)  
            ecrire_info()
    if list_weapon == "Exit":
        pass
    


### WALK BAR           
def walk():
    print("____________________________________________")
    print("Vous etes entrain de vous balader !")
    for i in tqdm(range(10)):
        sleep(0.1) #base 0.5
        
        
def walk2():
    print("____________________________________________")
    print("Vous etes entrain de le voir !")
    for i in tqdm(range(10)):
        sleep(0.1) #base 1
        
        
def save():
    for i in tqdm(range(10)):
        sleep(0.1) #base 1
        
### XPS
def xp_level_up():
    global levels_check
    global xp
    global levels
    global resistance
    global force
    if xp >= levels_check:
        xp = 0
        levels_check += 20
        levels += 1 
        ecrire_info()
        print("Bravo vous etes niveau {}".format(levels))
        ask_speciality_updates = input("Que voulez vous améliorer ? (force/resistance)\n> ")
        if ask_speciality_updates == "force":
            print("____________________________________________")
            force += 1
            print("Vous avez gagnez 1 niveau de FORCE")
            print("Force > ",force, "\nXp Next Level > ",levels_check)
            ecrire_info()
            print("____________________________________________")
        if ask_speciality_updates == "resistance":
            print("____________________________________________")
            resistance += 1
            print("Vous avez gagnez 1 niveau de RESISTANCE")
            print("Resistance > ",resistance, "\nXp Next Level > ",levels_check)
            ecrire_info()
            print("____________________________________________")
        
### MOBS     
def fight_blob(blob_niv1, healt):
    global levels_check
    global force
    global resistance
    global levels
    global xp
    global wallet
    global couteau_buy
    global sword_buy
    global pistole_buy
    while True:
        ask_attack_blob = input("Voulez vous l'attaquer ? (Oui/Non)\nSTATS\nPv : 10\nDegat : 5\n> ")
        if ask_attack_blob == "Oui":
            while True:
                if xp >= levels_check:
                    xp_level_up()
                else:
                    pass
                if blob_niv1 == 0:
                    print("____________________________________________")
                    print(blob_niv1)
                    print('Vous avez gagnez !')
                    xp += 5
                    wallet += 20
                    healt = 20
                    print("Vous gagnez 20$ + ",xp,"XP, TOTAL : ",wallet,"$ XP : ",xp)
                    blob_niv1 = 10
                    print("____________________________________________")
                    break
                if healt == 0:
                    print("____________________________________________")
                    print("Vos Pv : ",healt)
                    print("Vous avez perdu !")
                    sleep(2)
                    print("____________________________________________")
                    break
                if couteau_buy == False:
                    print("Vous n'avez pas d'arme !")
                    list_weapon(wallet, couteau_buy, sword_buy, pistole_buy)
                    break
                print("Blob Niv : 1\nPv : 10")
                print("Vous attacker !")
                sleep(1)
                if force >= 1:
                    if couteau_buy == True:
                        blob_niv1 -= 5 * force
                    if sword_buy == True:
                        blob_niv1 -= 10 * force
                    if pistole_buy == True:
                        blob_niv1 -= 15 * force
                else:
                    if couteau_buy == True:
                        blob_niv1 -= 5
                    if sword_buy == True:
                        blob_niv1 -= 10
                    if pistole_buy == True:
                        blob_niv1 -= 15
                print("Pv Blob: ",blob_niv1) 
                print("Il vous attack !")
                sleep(1)
                if resistance >= 1:
                    healt -= 5 / resistance                     
                else:
                    healt -= 5

                print("Vos Pv: ",healt)
        else:
            pass
              
        ask_weapon_buy3 = input("Voulez vous voir le magasin ? (Oui/Non)\n> ")
        if ask_weapon_buy3 == "magasin":
            list_weapon()
        else:
            ask_walk_distance = input("Au loin vous voyez un monstre, voulez vous l'attaquer ? (Oui/Exit)\n> ")
            if ask_walk_distance == "Oui":
                walk2()
                if random.randint(0, 1) == 0:
                    print("____________________________________________")
                    print("Vous avez trouvez un BLOB")
                    sleep(1)
                    print("____________________________________________")
                    fight_blob(blob_niv1, healt)
                else:
                    print("____________________________________________")
                    print("Vous avez trouver un SORCIER")
                    sleep(1)
                    print("____________________________________________")
                    fight_sorcier(sorcier_niv1, healt)
            if ask_walk_distance == "Exit":
                print("Sauvegarde ! (Veilliez ne pas fermer)")
                ecrire_info()
                save()
                exit(0)
                
    
def fight_sorcier(sorcier_niv1, healt):
    global levels_check
    global xp
    global wallet
    global couteau_buy
    global sword_buy
    global pistole_buy
    while True:
        ask_attack_sorcier = input("Voulez vous l'attaquer ? (Oui/Non)\nSTATS\nPv : 20\nDegat : 10\n> ")
        if ask_attack_sorcier == "Oui":
            while True:
                if xp >= levels_check:
                    xp_level_up()
                else:
                    pass
                if sorcier_niv1 == 0:
                    print("____________________________________________")
                    print(sorcier_niv1)
                    print('Vous avez gagnez !')
                    xp += 10
                    wallet += 40
                    healt = 20
                    print("Vous gagnez 40$ + ",xp,"XP TOTAL : ",wallet,"$ XP : ",xp)
                    sorcier_niv1 = 20
                    print("____________________________________________")
                    break
                if healt == 0:
                    print("____________________________________________")
                    print("> Vos Pv : ",healt)
                    print("Vous avez perdu !")
                    sleep(2)
                    print("____________________________________________")
                    break
                if couteau_buy == False:
                    print("Vous n'avez pas d'arme !")
                    list_weapon(wallet, couteau_buy, sword_buy, pistole_buy)
                    break
                print("Sorcier Niv : 1\nPv : 10")
                print("Vous attacker !")
                sleep(1)
                if force >= 1:
                    if couteau_buy == True:
                        blob_niv1 -= 5 * force
                    if sword_buy == True:
                        blob_niv1 -= 10 * force
                    if pistole_buy == True:
                        blob_niv1 -= 15 * force
                else:
                    if couteau_buy == True:
                        blob_niv1 -= 5
                    if sword_buy == True:
                        blob_niv1 -= 10
                    if pistole_buy == True:
                        blob_niv1 -= 15
                print("Pv Sorcier: ",sorcier_niv1)  
                print("Il vous attack !")
                sleep(1)
                if resistance >= 1:
                    healt -= 10 / resistance
                else:
                    healt -= 10
                print("Vos Pv: ",healt)
        else:
            pass   
        
        ask_weapon_buy3 = input("Voulez vous voir le magasin ? (Oui/Non)\n> ")
        if ask_weapon_buy3 == "magasin":
            list_weapon()
        else:
            ask_walk_distance = input("Au loin vous voyez un monstre, voulez vous l'attaquer ? (Oui/Exit)\n> ")
            if ask_walk_distance == "Oui":
                walk2()
                if random.randint(0, 1) == 0:
                    print("____________________________________________")
                    print("Vous avez trouvez un BLOB")
                    sleep(1)
                    print("____________________________________________")
                    fight_blob(blob_niv1, healt)
                else:
                    print("____________________________________________")
                    print("Vous avez trouver un SORCIER")
                    sleep(1)
                    print("____________________________________________")
                    fight_sorcier(sorcier_niv1, healt)
            if ask_walk_distance == "Exit":
                print("Sauvegarde ! (Veilliez ne pas fermer)")
                ecrire_info()
                save()
                exit(0)
walk()

ask_weapon_png = input("Vous avez vu un vendeur d'arme vous voulez le voir ? (Oui/Non)\n> ")
if ask_weapon_png == "Oui":
    walk()
    ask_weapon = input("Vous voulez achetez une arme vous avez {}$ ? (Oui/Non)\n>".format(wallet))
    if ask_weapon == "Oui":
        list_weapon()
    if couteau_buy == False:
        print("Vous devez avoir une arme pour avancer")
        list_weapon()
else:
    pass
    ### ASK WEAPON START




ask_walk_distance = input("Au loin vous voyez un monstre vous voulez l'attacker ? (Oui/Non)\n> ")
if ask_walk_distance == "Oui":
    walk2()
    if random.randint(0, 1) == 0:
        print("____________________________________________")
        print("Vous avez trouvez un BLOB")
        sleep(1)
        print("____________________________________________")
        fight_blob(blob_niv1, healt)
    else:
        print("____________________________________________")
        print("Vous avez trouver un SORCIER")
        sleep(1)
        print("____________________________________________")
        fight_sorcier(sorcier_niv1, healt)
else:
    print("____________________________________________")
    print("Fin de la beta !")
    




