### IMPORT
from enum import Flag
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

# marchand quete
weapon_png_2 = False
oynix_boss = False
the_end_boss_activated = False

oynix_win = False
### QUETES
x_blob_kill = 0 #10 blobs / 50 pieces
x_blob_kill_running = False
xx_sorcier_kill = 0 #20 sorciers / 500 pieces
xx_sorcier_kill_running = False

force_niveaux_10 = False
resistance_niveaux_10 = False

### ### XP +
force = 0
resistance = 0


healt = 20
wallet = 50

couteau = 50 # Degat 5
sword = 100 # Degat 10
pistole = 150 # Degat 20

armor_fer = 500 # /0.5
armor_or = 1000 # /1
armor_diamant = 2000 #/2

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

the_destructor = False
the_ice_of_king = False
the_neant = False

the_destructor_prix = 5000 # Degats : 50
the_ice_of_king_prix = 12000 # Degats : 100
the_neant_prix = 40000 # Degats : 200

fight_blob_niv1 = False

# BOSS DONNE
oynix_life = 20000 # Degats : 100
the_end_boss_life = 40000 # Degats : 200 Condition : [tuez Oynix + 400 000 pieces au marchand ]
                                  

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
        json.dump(str({'name:': player, 'force:': force, 'resistance:': resistance, 'Pv:': healt, 'Money:': wallet, 'Couteau:': couteau, 'Epee:': sword, 'Pistolet': pistole, 'Xp:': xp, 'Levels:': levels, 'Levels_Check:': levels_check, 'Couteau_Buy': couteau_buy, 'Sword_Buy:': sword_buy, 'Gun_Buy:': pistole_buy, 'Armor_Fer_Buy': armor_fer_buy, 'Armor_Or_Buy': armor_or_buy, 'Armor_Diamond_Buy': armor_diamant_buy}), fichier)
### BOSS
def end_the_end():
    print(""" 
                                                                          
      _____        _____          ____    ____      ____         _____    
 ___|\     \   ___|\    \    ____|\   \  |    |    |    |   ____|\    \   
|    |\     \ |    |\    \  /    /\    \ |    |    |    |  /     /\    \  
|    | |     ||    | |    ||    |  |    ||    |    |    | /     /  \    \ 
|    | /_ _ / |    |/____/ |    |__|    ||    |    |    ||     |    |    |
|    |\    \  |    |\    \ |    .--.    ||    |    |    ||     |    |    |
|    | |    | |    | |    ||    |  |    ||\    \  /    /||\     \  /    /|
|____|/____/| |____| |____||____|  |____|| \ ___\/___ / || \_____\/____/ |
|    /     || |    | |    ||    |  |    | \ |   ||   | /  \ |    ||    | /
|____|_____|/ |____| |____||____|  |____|  \|___||___|/    \|____||____|/ 
  \(    )/      \(     )/    \(      )/      \(    )/         \(    )/    
   '    '        '     '      '      '        '    '           '    '     
                                                                          
""")
    sleep(0.5)
    print("                Vous avez battue le boss FINAL")
    sleep(1.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                Mais cela ne que le début d'une grande aventure")
    sleep(2)
    print(""" 
 ▄▄▄▄    ▒█████   ███▄    █  ███▄    █ ▓█████     ▄████▄   ██░ ██  ▄▄▄       ███▄    █  ▄████▄  ▓█████ 
▓█████▄ ▒██▒  ██▒ ██ ▀█   █  ██ ▀█   █ ▓█   ▀    ▒██▀ ▀█  ▓██░ ██▒▒████▄     ██ ▀█   █ ▒██▀ ▀█  ▓█   ▀ 
▒██▒ ▄██▒██░  ██▒▓██  ▀█ ██▒▓██  ▀█ ██▒▒███      ▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄ ▒███   
▒██░█▀  ▒██   ██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄    ▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒▓█  ▄ 
░▓█  ▀█▓░ ████▓▒░▒██░   ▓██░▒██░   ▓██░░▒████▒   ▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░░▒████▒
░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░░ ▒░ ░
▒░▒   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░     ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒    ░ ░  ░
 ░    ░ ░ ░ ░ ▒     ░   ░ ░    ░   ░ ░    ░      ░         ░  ░░ ░  ░   ▒      ░   ░ ░ ░           ░   
 ░          ░ ░           ░          ░    ░  ░   ░ ░       ░  ░  ░      ░  ░         ░ ░ ░         ░  ░
      ░                                          ░                                     ░                 
""")
    ask_weapon_buy3 = input("Voulez vous voir qu'elle magasin  ? (Armes/Armures/Quetes/Enter = Exit)\n> ")
    if ask_weapon_buy3 == "Armes":
        list_weapon()
    if ask_weapon_buy3 == "Armures":
        list_armor()
    if ask_weapon_buy3 == "Quetes":
        shop_quest()

    if weapon_png_2 == True:
        ask_new_png_weapon = input("Voulez voir le marchand supreme ? (Oui/Non)\n> ")
        if ask_new_png_weapon == "Oui":
            marchand_weapon2()
        if ask_new_png_weapon == "Non":
            pass
    else:
        ask_walk_distance = input("Au loin vous voyez un monstre, voulez vous l'attaquer ? (Oui/Exit)\n> ")
        if ask_walk_distance == "Oui":
            walk2()
            if random.randint(0, 1) == 0:
                print("____________________________________________")
                print("Vous avez trouvez un BLOB")
                sleep(1)
                print("____________________________________________")
                fight_blob()
            else:
                print("____________________________________________")
                print("Vous avez trouver un SORCIER")
                sleep(1)
                print("____________________________________________")
                fight_sorcier()
        if ask_walk_distance == "Exit":
            print("Sauvegarde ! (Veilliez ne pas fermer)")
            ecrire_info()
            save()
            exit(0)
def oynix_start():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("""
         _______               _____                    _____                    _____                                  
        /::\    \             |\    \                  /\    \                  /\    \                 ______          
       /::::\    \            |:\____\                /::\____\                /::\    \               |::|   |         
      /::::::\    \           |::|   |               /::::|   |                \:::\    \              |::|   |         
     /::::::::\    \          |::|   |              /:::::|   |                 \:::\    \             |::|   |         
    /:::/~~\:::\    \         |::|   |             /::::::|   |                  \:::\    \            |::|   |         
   /:::/    \:::\    \        |::|   |            /:::/|::|   |                   \:::\    \           |::|   |         
  /:::/    / \:::\    \       |::|   |           /:::/ |::|   |                   /::::\    \          |::|   |         
 /:::/____/   \:::\____\      |::|___|______    /:::/  |::|   | _____    ____    /::::::\    \         |::|   |         
|:::|    |     |:::|    |     /::::::::\    \  /:::/   |::|   |/\    \  /\   \  /:::/\:::\    \  ______|::|___|___ ____ 
|:::|____|     |:::|    |    /::::::::::\____\/:: /    |::|   /::\____\/::\   \/:::/  \:::\____\|:::::::::::::::::|    |
 \:::\    \   /:::/    /    /:::/~~~~/~~      \::/    /|::|  /:::/    /\:::\  /:::/    \::/    /|:::::::::::::::::|____|
  \:::\    \ /:::/    /    /:::/    /          \/____/ |::| /:::/    /  \:::\/:::/    / \/____/  ~~~~~~|::|~~~|~~~      
   \:::\    /:::/    /    /:::/    /                   |::|/:::/    /    \::::::/    /                 |::|   |         
    \:::\__/:::/    /    /:::/    /                    |::::::/    /      \::::/____/                  |::|   |         
     \::::::::/    /     \::/    /                     |:::::/    /        \:::\    \                  |::|   |         
      \::::::/    /       \/____/                      |::::/    /          \:::\    \                 |::|   |         
       \::::/    /                                     /:::/    /            \:::\    \                |::|   |         
        \::/____/                                     /:::/    /              \:::\____\               |::|   |         
         ~~                                           \::/    /                \::/    /               |::|___|         
                                                       \/____/                  \/____/                 ~~              
                                                                                                                        


    """)
    ask_boss_attack = input("                        Vous voulez vous l'attacker?\n                                 Oui/Non\n                                  > ")
    if ask_boss_attack == "Oui":
        oynix_fight()
    else:
        pass

def theendstart():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("""
                                                                                         
 _________________  ____   ____      ______        ______  _____   ______        _____   
/                 \|    | |    | ___|\     \   ___|\     \|\    \ |\     \   ___|\    \  
\______     ______/|    | |    ||     \     \ |     \     \\\    \| \     \ |    |\    \ 
   \( /    /  )/   |    |_|    ||     ,_____/||     ,_____/|\|    \  \     ||    | |    |
    ' |   |   '    |    .-.    ||     \--'\_|/|     \--'\_|/ |     \  |    ||    | |    |
      |   |        |    | |    ||     /___/|  |     /___/|   |      \ |    ||    | |    |
     /   //        |    | |    ||     \____|\ |     \____|\  |    |\ \|    ||    | |    |
    /___//         |____| |____||____ '     /||____ '     /| |____||\_____/||____|/____/|
   |`   |          |    | |    ||    /_____/ ||    /_____/ | |    |/ \|   |||    /    | |
   |____|          |____| |____||____|     | /|____|     | / |____|   |___|/|____|____|/ 
     \(              \(     )/    \( |_____|/   \( |_____|/    \(       )/    \(    )/   
      '               '     '      '    )/       '    )/        '       '      '    '    
                                        '             '                                      
    """)
    ask_boss_attack_end = input("                        Vous voulez vous l'attacker?\n                                 Oui/Non\n                                  > ")
    if ask_boss_attack_end == "Oui":
        the_end_fight()
    else:
        pass

def oynix_fight():
    global healt
    global oynix_life
    global oynix_win
    global levels_check
    global the_neant
    global force
    global resistance
    global levels
    global xp
    global the_destructor
    global the_ice_of_king
    global the_end_boss_activated
    global player
    global wallet
    global couteau_buy
    global sword_buy
    global pistole_buy
    while True:
        ask_attack_oynix = input("Voulez vous l'attaquer ? (Oui/Non)\nSTATS\nPv : 20 000\nDegat : 100\n> ")
        if ask_attack_oynix == "Oui":
            while True:
                if xp >= levels_check:
                    xp_level_up()
                else:
                    pass
                quest_checks()
                if oynix_life == 0:
                    print("Bien jouer {}".format(player))
                    sleep(0.5)
                    print("Je reviendrais mes plus FORT !")
                    sleep(0.2)
                    print("____________________________________________")
                    print(oynix_life)
                    print('Vous avez gagnez !')
                    force += 6
                    resistance += 6
                    the_end_boss_activated = True
                    wallet += 15000
                    oynix_win = True
                    healt = 20
                    print("Vous gagnez 15000$ + ",xp,"XP, TOTAL : ",wallet,"$ XP : ",xp)
                    oynix_life = 20000
                    print("____________________________________________")
                    break
                if healt == 0:
                    print("____________________________________________")
                    print("Vos Pv : ",healt)
                    print("Vous avez perdu !")
                    sleep(2)
                    print("____________________________________________")
                    break
                print("Blob Niv : 1\nPv : 10")
                print("Vous attacker !")
                sleep(1)
                if force >= 1:
                    if couteau_buy == True:
                        oynix_life -= 5 * force
                    if sword_buy == True:
                        oynix_life -= 10 * force
                    if pistole_buy == True:
                        oynix_life -= 15 * force
                    if the_destructor == True:
                        oynix_life -= 50 * force
                    if the_ice_of_king == True:
                        oynix_life -= 100 * force
                    if the_neant == True:
                        oynix_life -= 200 * force
                else:
                    if couteau_buy == True:
                        oynix_life -= 5
                    if sword_buy == True:
                        oynix_life -= 10
                    if pistole_buy == True:
                        oynix_life -= 15
                    if the_destructor == True:
                        oynix_life -= 50
                    if the_ice_of_king == True:
                        oynix_life -= 100
                    if the_neant == True:
                        oynix_life -= 200
                print("Pv Blob: ",oynix_life) 
                print("Il vous attack !")
                sleep(1)
                if resistance >= 1:
                    healt -= 100 / resistance
                    if armor_fer_buy == True:
                        healt += 1
                    if armor_or_buy == True:
                        healt += 2
                    if armor_diamant_buy == True:
                        healt += 3                          
                else:
                    if armor_fer_buy == True:
                        healt -= 100 / 0.5
                    if armor_or_buy == True:
                        healt -= 100 / 1
                    if armor_diamant_buy == True:
                        healt -= 100 / 2
                    else:
                        healt -= 5
                print("Vos Pv: ",healt)
        else:
            pass
              
        ask_weapon_buy3 = input("Voulez vous voir qu'elle magasin  ? (Armes/Armures/Quetes/Enter = Exit)\n> ")
        if ask_weapon_buy3 == "Armes":
            list_weapon()
        if ask_weapon_buy3 == "Armures":
            list_armor()
        if ask_weapon_buy3 == "Quetes":
            shop_quest()

        if weapon_png_2 == True:
            ask_new_png_weapon = input("Voulez voir le marchand supreme ? (Oui/Non)\n> ")
            if ask_new_png_weapon == "Oui":
                marchand_weapon2()
            if ask_new_png_weapon == "Non":
                pass
        else:
            ask_walk_distance = input("Au loin vous voyez un monstre, voulez vous l'attaquer ? (Oui/Exit)\n> ")
            if ask_walk_distance == "Oui":
                walk2()
                if random.randint(0, 1) == 0:
                    print("____________________________________________")
                    print("Vous avez trouvez un BLOB")
                    sleep(1)
                    print("____________________________________________")
                    fight_blob()
                else:
                    print("____________________________________________")
                    print("Vous avez trouver un SORCIER")
                    sleep(1)
                    print("____________________________________________")
                    fight_sorcier()
            if ask_walk_distance == "Exit":
                print("Sauvegarde ! (Veilliez ne pas fermer)")
                ecrire_info()
                save()
                exit(0)
### 
def the_end_fight():
    global healt
    global the_end_boss_life
    global the_end_boss_activated
    global levels_check
    global the_neant
    global force
    global resistance
    global levels
    global xp
    global the_destructor
    global the_ice_of_king
    global player
    global wallet
    global couteau_buy
    global sword_buy
    global pistole_buy
    while True:
        ask_attack_end = input("Voulez vous l'attaquer ? (Oui/Non)\nSTATS\nPv : 40 000\nDegat : 200\n> ")
        if ask_attack_end == "Oui":
            while True:
                if xp >= levels_check:
                    xp_level_up()
                else:
                    pass
                quest_checks()
                if the_end_boss_life == 0:
                    print("Bien jouer {}".format(player))
                    sleep(0.5)
                    print("Tu crois que cela est finis Alors que cela n'es faux")
                    sleep(0.2)
                    print("____________________________________________")
                    print(oynix_life)
                    print('Vous avez gagnez !')
                    force += 20
                    resistance += 20
                    wallet += 65000
                    oynix_win = True
                    healt = 20
                    print("Vous gagnez 65000$ + ",xp,"XP, TOTAL : ",wallet,"$ XP : ",xp)
                    oynix_life = 20000
                    print("____________________________________________")
                    break
                if healt == 0:
                    print("____________________________________________")
                    print("Vos Pv : ",healt)
                    print("Vous avez perdu !")
                    sleep(2)
                    print("____________________________________________")
                    break
                print("Blob Niv : 1\nPv : 10")
                print("Vous attacker !")
                sleep(1)
                if force >= 1:
                    if couteau_buy == True:
                        the_end_boss_life -= 5 * force
                    if sword_buy == True:
                        the_end_boss_life -= 10 * force
                    if pistole_buy == True:
                        the_end_boss_life -= 15 * force
                    if the_destructor == True:
                        the_end_boss_life -= 50 * force
                    if the_ice_of_king == True:
                        the_end_boss_life -= 100 * force
                    if the_neant == True:
                        the_end_boss_life -= 200 * force
                else:
                    if couteau_buy == True:
                        the_end_boss_life -= 5
                    if sword_buy == True:
                        the_end_boss_life -= 10
                    if pistole_buy == True:
                        the_end_boss_life -= 15
                    if the_destructor == True:
                        the_end_boss_life -= 50
                    if the_ice_of_king == True:
                        the_end_boss_life -= 100
                    if the_neant == True:
                        the_end_boss_life -= 200
                print("Pv The End: ",the_end_boss_life) 
                print("Il vous attack !")
                sleep(1)
                if resistance >= 1:
                    healt -= 100 / resistance
                    if armor_fer_buy == True:
                        healt += 1
                    if armor_or_buy == True:
                        healt += 2
                    if armor_diamant_buy == True:
                        healt += 3                          
                else:
                    if armor_fer_buy == True:
                        healt -= 100 / 0.5
                    if armor_or_buy == True:
                        healt -= 100 / 1
                    if armor_diamant_buy == True:
                        healt -= 100 / 2
                    else:
                        healt -= 5
                print("Vos Pv: ",healt)
        else:
            pass
        end_the_end()      




### START
print("Bienvenue",player," Vous avez ",wallet,"$ Votre nombre de vie ",healt,"pv")

### DEF

def marchand_weapon2():
    global wallet
    global the_destructor_prix
    global the_destructor
    global the_end_boss_activated
    global the_ice_of_king_prix
    global couteau_buy
    global sword_buy
    global pistole_buy
    global the_neant
    global the_neant_prix
    global oynix_win
    global the_ice_of_king
    print("____________________________________________")
    ask_weapon2 = input("Vous voulez qu'elle arme ?\n1: The Destructor (Degats: 50/Prix: 5000)\n2: The Ice of King (Degats: 100/Prix: 12 000)\n3: The Neant (Degats:200/Prix:40 000\n4:Lists boss\n1 ou 2 ou 3 ou 4Exit\n> ")
    if ask_weapon2 == "1":
        if wallet < 5000:
            print("Vous n'avez pas 50 $, votre argent {}$".format(wallet))
        if wallet >= 5000:
            couteau_buy=False
            sword_buy=False
            pistole_buy=False
            wallet -= the_destructor_prix
            the_destructor=True
            print("Il vous reste, {}$".format(wallet))
            print("____________________________________________")
    if ask_weapon2 == "2":
        if wallet < 12000:
            print("Vous n'avez pas 50 $, votre argent {}$".format(wallet))
        if wallet >= 12000:
            couteau_buy=False
            sword_buy=False
            pistole_buy=False
            the_destructor=False
            wallet -= the_ice_of_king_prix
            the_ice_of_king=True
            print("Il vous reste, {}$".format(wallet))
            print("____________________________________________")
    if ask_weapon2 == "3":
        if wallet < 40000:
            print("Vous n'avez pas 50 $, votre argent {}$".format(wallet))
        if wallet >= 40000:
            if oynix_win == True:
                couteau_buy=False
                sword_buy=False
                pistole_buy=False
                the_destructor=False
                wallet -= the_neant_prix
                the_ice_of_king=False
                the_neant = True
                print("Il vous reste, {}$".format(wallet))
                print("____________________________________________")
        else:
            print("Vous n'avez pas vaincu le boss OYNIX")
            marchand_weapon2()
    if ask_weapon2 == "4":
        ask_boss_buy = input("Vous voulez qu'elle boss \nOynix \ Vie : 20 000 \ Degats : 100\nThe End \ Vie : 40 000 \ Degats: 200 \ Prix : 400 000$\nOynix or TheEnd ?\n> ")
        if ask_boss_buy == "Oynix":
            print("Bonne chance !")
            sleep(0.2)
            oynix_fight()
        if ask_boss_buy == "TheEnd":
            if the_end_boss_activated == True:
                if wallet < 400000:
                    print("Vous n'avez pas assez d'argent il vous faut 400 000$\nVous avez {}".format(wallet))
                if wallet >= 400000:
                    print("Bon Combat !")
                    sleep(0.2)
                    theendstart()
            else:
                print("Vous n'avez pas debloquez le boss\nVeilliez tuez le Oynix en premier")
    if ask_weapon2 == "Exit":
        pass
    
# QUETES (1partie)
def shop_quest():
    global x_blob_kill_running
    global xx_sorcier_kill_running
    global force_niveaux_10
    global resistance_niveaux_10
    ask_quete_shop = input("Hey vous voulez voir les quetes ? (Oui/Non)\n> ")
    if ask_quete_shop == "Oui":
        print("\n")
        ask_choice_quete = input("Voici la listes des quetes\n1:Tuez 10 Blobs\n2:Tuez 20 sorciers\n3: Quetes a 2 parties\n1 ou 2 ou 3 ?\n> ")
        if ask_choice_quete == "1":
            print("____________________________________________")
            x_blob_kill_running=True
            print(x_blob_kill_running)
            print("Vous avez pris la quete des 10 blobs\nRécompense : 50$\nBonne Chance!")
            print("____________________________________________")
        if ask_choice_quete == "2":
            print("____________________________________________")
            xx_sorcier_kill_running=True
            print(xx_sorcier_kill_running)
            print("Vous avez pris la quete des 20 sorciers\nRécompense : 800$\nBonne Chance!")
            print("____________________________________________")
        if ask_choice_quete == "3":
            print("____________________________________________")
            ask_choice_quete_2party = input("Voici la quete a deux parties\n1:Force Niveaux 10/Resistance Niveaux 10\n(Oui/Non) ?\n> ")
            print("____________________________________________")
            if ask_choice_quete_2party == "Oui":
                print("____________________________________________")
                force_niveaux_10=True
                resistance_niveaux_10=True
                print("Bonne chance !")
                print("____________________________________________")
            if ask_choice_quete_2party == "Non":
                pass
            
### SHOP 
def list_weapon():
    global wallet
    global couteau_buy
    global the_destructor
    global the_ice_of_king
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
            couteau_buy=False
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
            couteau_buy=False
            sword_buy=False
            ecrire_info()
    if list_weapon == "Exit":
        pass
    
    
def list_armor():
    global armor_or
    global armor_fer
    global armor_diamant
    global wallet
    global armor_diamant_buy
    global armor_fer_buy
    global armor_or_buy
    list_weapon = input("Voici la liste des armes ! \n1: Armure En Fer\n2: Armure En Or\n3: Armure En Diamant\n4: Exit\n(Repondez par (Fer/Or/Diamant))\n> ")
    if list_weapon == "Fer":
        if wallet < 500:
            print("Vous n'avez pas 500 $, votre argent {}$".format(wallet))
        if wallet >= 500:
            wallet -= armor_fer
            print("Vous avez une Armure en Fer !")
            print("Il vous reste {}".format(wallet))
            armor_fer_buy=True
            print(armor_fer_buy)
            ecrire_info()
    if list_weapon == "Or":
        if wallet < 1000:
            print("Vous n'avez pas 1000 $, votre argent {}$".format(wallet))
        if wallet >= 1000:
            wallet -= armor_or
            print("Vous avez une Armure en Or !")
            print("Il vous reste {}".format(wallet))
            armor_or_buy=True
            armor_fer_buy = False
            print(armor_or_buy)
            ecrire_info()
    if list_weapon == "Diamant":
        if wallet < 2000:
            print("Vous n'avez pas 2000 $, votre argent {}$".format(wallet))
        if wallet >= 2000:
            wallet -= armor_diamant    
            print("Vous avez une Armure en Diamant !")
            print("Il vous reste {}".format(wallet))
            armor_diamant_buy=True
            armor_fer_buy=False
            armor_or_buy=False
            print(armor_diamant_buy)  
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
    global healt
    global levels
    global resistance
    global force
    if xp >= levels_check:
        xp = 0
        levels_check += 20
        levels += 1 
        ecrire_info()
        print("Bravo vous etes niveau {}".format(levels))
        ask_speciality_updates = input("Que voulez vous améliorer ? (force/resistance/healt)\n> ")
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
        if ask_speciality_updates == "healt":
            if weapon_png_2 == True:
                print("____________________________________________")
                healt * 2
                print("Vous avez gagnez 1 niveau de HEALT")
                print("Resistance > ",healt, "\nXp Next Level > ",levels_check)
                ecrire_info()
                print("____________________________________________")
            if weapon_png_2 == False:
                print("Vous n'avez pas fait la quête à deux parties !")
                pass
        

def quest_checks():
    global wallet
    global oynix_boss
    global weapon_png_2
    global force
    global resistance
    global x_blob_kill_running  
    global x_blob_kill
    global xx_sorcier_kill_running
    global xx_sorcier_kill
    if x_blob_kill_running == True:
        if x_blob_kill >= 10:
            wallet += 50
            x_blob_kill_running = False
            print("__________________________________________________________")
            print("Bravo vous avez finis la quete des 10 blobs gagnez 50$, {}".format(wallet))
            print("__________________________________________________________")
        else:
            pass
    if xx_sorcier_kill_running == True:
        if xx_sorcier_kill >= 20:
            wallet += 500
            xx_sorcier_kill_running = False
            print("______________________________________________________________")
            print("Bravo vous avez finis la quete des 20 sorciers gagnez 500$, {}".format(wallet))
            print("______________________________________________________________")
        else:
            pass
    if force >= 10:
        if resistance >= 10:
            oynix_boss = True
            weapon_png_2 = True
            print("______________________________________________________________")
            print("BRAVO *claps*claps*\nVous avez finis la quete!\nVous debloquez un nouveau marchand et un nouveau Boss (Oynix)")
            print("______________________________________________________________")       
            marchand_weapon2()
    else:
        pass

### MOBS     
def fight_blob():
    global healt
    global the_neant
    global blob_niv1
    global levels_check
    global force
    global resistance
    global levels
    global x_blob_kill
    global xp
    global the_destructor
    global the_ice_of_king
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
                quest_checks()
                if blob_niv1 == 0:
                    print("____________________________________________")
                    print(blob_niv1)
                    print('Vous avez gagnez !')
                    xp += 5
                    wallet += 20
                    healt = 20
                    print("Vous gagnez 20$ + ",xp,"XP, TOTAL : ",wallet,"$ XP : ",xp)
                    blob_niv1 = 10
                    x_blob_kill += 1
                    print("____________________________________________")
                    break
                if healt == 0:
                    print("____________________________________________")
                    print("Vos Pv : ",healt)
                    print("Vous avez perdu !")
                    sleep(2)
                    print("____________________________________________")
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
                    if the_destructor == True:
                        blob_niv1 -= 50 * force
                    if the_ice_of_king == True:
                        blob_niv1 -= 100 * force
                    if the_neant == True:
                        blob_niv1 -= 200 * force   
                else:
                    if couteau_buy == True:
                        blob_niv1 -= 5
                    if sword_buy == True:
                        blob_niv1 -= 10
                    if pistole_buy == True:
                        blob_niv1 -= 15
                    if the_destructor == True:
                        blob_niv1 -= 50
                    if the_ice_of_king == True:
                        blob_niv1 -= 100
                    if the_neant == True:
                        blob_niv1 -= 200
                print("Pv Blob: ",blob_niv1) 
                print("Il vous attack !")
                sleep(1)
                if resistance >= 1:
                    healt -= 5 / resistance
                    if armor_fer_buy == True:
                        healt += 1
                    if armor_or_buy == True:
                        healt += 2
                    if armor_diamant_buy == True:
                        healt += 3                          
                else:
                    if armor_fer_buy == True:
                        healt -= 5 / 0.5
                    if armor_or_buy == True:
                        healt -= 5 / 1
                    if armor_diamant_buy == True:
                        healt -= 5 / 2
                    else:
                        healt -= 5
                print("Vos Pv: ",healt)
        else:
            pass
              
        ask_weapon_buy3 = input("Voulez vous voir qu'elle magasin  ? (Armes/Armures/Quetes/Enter = Exit)\n> ")
        if ask_weapon_buy3 == "Armes":
            list_weapon()
        if ask_weapon_buy3 == "Armures":
            list_armor()
        if ask_weapon_buy3 == "Quetes":
            shop_quest()

        if weapon_png_2 == True:
            ask_new_png_weapon = input("Voulez voir le marchand supreme ? (Oui/Non)\n> ")
            if ask_new_png_weapon == "Oui":
                marchand_weapon2()
            if ask_new_png_weapon == "Non":
                pass
        else:
            if oynix_boss == True:
                ask_boss_attack = input("Vous voulez vous attacker le boss OYNIX ? (Oui/Non)\n> ")
                if ask_attack_blob == "Oui":
                    oynix_fight()
                if ask_attack_blob == "Non":
                    pass
                else:
                    pass
            ask_walk_distance = input("Au loin vous voyez un monstre, voulez vous l'attaquer ? (Oui/Exit)\n> ")
            if ask_walk_distance == "Oui":
                walk2()
                if random.randint(0, 1) == 0:
                    print("____________________________________________")
                    print("Vous avez trouvez un BLOB")
                    sleep(1)
                    print("____________________________________________")
                    fight_blob()
                else:
                    print("____________________________________________")
                    print("Vous avez trouver un SORCIER")
                    sleep(1)
                    print("____________________________________________")
                    fight_sorcier()
            if ask_walk_distance == "Exit":
                print("Sauvegarde ! (Veilliez ne pas fermer)")
                ecrire_info()
                save()
                exit(0)
    
    
def fight_sorcier():
    global healt
    global sorcier_niv1
    global levels_check
    global the_destructor
    global the_ice_of_king
    global the_neant
    global xp
    global wallet
    global couteau_buy
    global sword_buy
    global xx_sorcier_kill
    global pistole_buy
    while True:
        ask_attack_sorcier = input("Voulez vous l'attaquer ? (Oui/Non)\nSTATS\nPv : 20\nDegat : 10\n> ")
        if ask_attack_sorcier == "Oui":
            while True:
                if xp >= levels_check:
                    xp_level_up()
                else:
                    pass
                quest_checks()
                if sorcier_niv1 == 0:
                    print("____________________________________________")
                    print(sorcier_niv1)
                    print('Vous avez gagnez !')
                    xp += 10
                    wallet += 40
                    healt = 20
                    print("Vous gagnez 40$ + ",xp,"XP TOTAL : ",wallet,"$ XP : ",xp)
                    sorcier_niv1 = 20
                    xx_sorcier_kill += 1
                    print("____________________________________________")
                    break
                if healt == 0:
                    print("____________________________________________")
                    print("> Vos Pv : ",healt)
                    print("Vous avez perdu !")
                    sleep(2)
                    print("____________________________________________")
                    break
                print("Sorcier Niv : 1\nPv : 10")
                print("Vous attacker !")
                sleep(1)
                if force >= 1:
                    if couteau_buy == True:
                        sorcier_niv1 -= 5 * force
                    if sword_buy == True:
                        sorcier_niv1 -= 10 * force
                    if pistole_buy == True:
                        sorcier_niv1 -= 15 * force
                    if the_destructor == True:
                        sorcier_niv1 -= 50 * force
                    if the_ice_of_king == True:
                        sorcier_niv1 -= 100 * force
                    if the_neant == True:
                        sorcier_niv1 -= 200 * force
                else:
                    if couteau_buy == True:
                        sorcier_niv1 -= 5
                    if sword_buy == True:
                        sorcier_niv1 -= 10
                    if pistole_buy == True:
                        sorcier_niv1 -= 15
                    if the_destructor == True:
                        sorcier_niv1 -= 50
                    if the_ice_of_king == True:
                        sorcier_niv1 -= 100
                    if the_neant == True:
                        sorcier_niv1 -= 200
                print("Pv Sorcier: ",sorcier_niv1)  
                print("Il vous attack !")
                sleep(1)
                if resistance >= 1:
                    healt -= 10 / resistance
                    if armor_fer_buy == True:
                        healt += 1
                    if armor_or_buy == True:
                        healt += 2
                    if armor_diamant_buy == True:
                        healt += 3                          
                else:
                    if armor_fer_buy == True:
                        healt -= 10 / 0.5
                    if armor_or_buy == True:
                        healt -= 10 / 1
                    if armor_diamant_buy == True:
                        healt -= 10 / 2
                    else:
                        healt -= 5
                print("Vos Pv: ",healt)
        else:
            pass   
        
        ask_weapon_buy3 = input("Voulez vous voir qu'elle magasin  ? (Armes/Armures/Quetes/Enter = Exit)\n> ")
        if ask_weapon_buy3 == "Armes":
            list_weapon()
        if ask_weapon_buy3 == "Armures":
            list_armor()
        if ask_weapon_buy3 == "Quetes":
            shop_quest()
            
        if weapon_png_2 == True:
            ask_new_png_weapon = input("Voulez voir le marchand supreme ? (Oui/Non)\n> ")
            if ask_new_png_weapon == "Oui":
                marchand_weapon2()
            if ask_new_png_weapon == "Non":
                pass
            
        else:
            ask_walk_distance = input("Au loin vous voyez un monstre, voulez vous l'attaquer ? (Oui/Exit)\n> ")
            if ask_walk_distance == "Oui":
                walk2()
                if random.randint(0, 1) == 0:
                    print("____________________________________________")
                    print("Vous avez trouvez un BLOB")
                    sleep(1)
                    print("____________________________________________")
                    fight_blob()
                else:
                    print("____________________________________________")
                    print("Vous avez trouver un SORCIER")
                    sleep(1)
                    print("____________________________________________")
                    fight_sorcier()
            if ask_walk_distance == "Exit":
                print("Sauvegarde ! (Veilliez ne pas fermer)")
                ecrire_info()
                save()
                exit(0)
walk()

ask_weapon_png = input("Vous avez vu un vendeur d'arme vous voulez le voir ? (Oui/Non/Enter)\n> ")
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

ask_armor_png = input("Vous avez vu un vendeur d'armure vous voulez le voir ? (Oui/Non)\n> ")
if ask_armor_png == "Oui":
    walk()
    ask_armor = input("Vous voulez achetez une armure vous avez {}$ ? (Oui/Non)\n>".format(wallet))
    if ask_armor == "Oui":
        list_armor()
    pass
    ### ASK WEAPON START

ask_quest_png = input("Vous voulez voir le vendeur des quetes ? (Oui/Non)\n> ")
if ask_quest_png == "Oui":
    walk()
    shop_quest()
if ask_quest_png == "Non":
    pass


ask_walk_distance = input("Au loin vous voyez un monstre vous voulez l'attacker ? (Oui/Non)\n> ")
if ask_walk_distance == "Oui":
    walk2()
    if random.randint(0, 1) == 0:
        print("____________________________________________")
        print("Vous avez trouvez un BLOB")
        sleep(1)
        print("____________________________________________")
        fight_blob()
    else:
        print("____________________________________________")
        print("Vous avez trouver un SORCIER")
        sleep(1)
        print("____________________________________________")
        fight_sorcier()
else:
    print("____________________________________________")
    print("Fin de la beta !")
    




