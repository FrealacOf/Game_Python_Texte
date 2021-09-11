wallet = 1000

x_blob_kill = 0
x_blob_kill_running = False
xx_sorcier_kill = 0
xx_sorcier_kill_running = False


def shop_quest():
    ask_quete_shop = input("Hey vous voulez voir les quetes ? (Oui/Non)\n> ")
    if ask_quete_shop == "Oui":
        print("\n")
        ask_choice_quete = input("Voici la listes des quetes\n1:Tuez 10 Blobs\n2:Tuez 20 sorciers\n1 ou 2 ?\n> ")
        if ask_choice_quete == "1":
            print("____________________________________________")
            x_blob_kill_running = True
            print(x_blob_kill_running)
            print("Vous avez pris la quete des 10 blobs\nRécompense : 50$\nBonne Chance!")
            print("____________________________________________")
        if ask_choice_quete == "2":
            print("____________________________________________")
            xx_sorcier_kill_running = True
            print(xx_sorcier_kill_running)
            print("Vous avez pris la quete des 20 sorciers\nRécompense : 800$\nBonne Chance!")
            print("____________________________________________")

shop_quest()