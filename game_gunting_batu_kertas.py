import random
import os
import time

daftar = ["Gunting","Batu","Kertas",
    "Gunting","Kertas","Batu",
    "Batu","Gunting","Kertas",
    "Batu","Kertas","Gunting",
    "Kertas","Gunting","Batu",
    "Kertas","Batu","Gunting",
    "Gunting","Batu","Kertas",
    "Gunting","Kertas","Batu",
    "Batu","Gunting","Kertas",
    "Batu","Kertas","Gunting",
    "Kertas","Gunting","Batu",
    "Kertas","Batu","Gunting",
    "Gunting","Batu","Kertas",
    "Gunting","Kertas","Batu",
    "Batu","Gunting","Kertas",
    "Batu","Kertas","Gunting",
    "Kertas","Gunting","Batu",
    "Kertas","Batu","Gunting",
    "Gunting","Batu","Kertas",
    "Gunting","Kertas","Batu",
    "Batu","Gunting","Kertas",
    "Batu","Kertas","Gunting",
    "Kertas","Gunting","Batu",
    "Kertas","Batu","Gunting",
    "Gunting","Batu","Kertas",
    "Gunting","Kertas","Batu",
    "Batu","Gunting","Kertas",
    "Batu","Kertas","Gunting",
    "Kertas","Gunting","Batu",
    "Kertas","Batu","Gunting",
    "Gunting","Batu","Kertas",
    "Gunting","Kertas","Batu",
    "Batu","Gunting","Kertas",
    "Batu","Kertas","Gunting",
    "Kertas","Gunting","Batu",
    "Kertas","Batu","Gunting",
    "Gunting","Batu","Kertas",
    "Gunting","Kertas","Batu",
    "Batu","Gunting","Kertas",
    "Batu","Kertas","Gunting",
    "Kertas","Gunting","Batu",
    "Kertas","Batu","Gunting",
    "Gunting","Batu","Kertas",
    "Gunting","Kertas","Batu",
    "Batu","Gunting","Kertas",
    "Batu","Kertas","Gunting",
    "Kertas","Gunting","Batu",
    "Kertas","Batu","Gunting",
    "Gunting","Batu","Kertas",
    "Gunting","Kertas","Batu",
    "Batu","Gunting","Kertas",
    "Batu","Kertas","Gunting",
    "Kertas","Gunting","Batu",
    "Kertas","Batu","Gunting"
]

def validasi_bot(pilih,bot):
    if pilih == "Gunting":
            if bot == "Gunting":
                return "Draw !"
            elif bot == "Batu":
                return "Anda Kalah !"
            elif bot == "Kertas":
                return "Anda Menang !"
            else :
                pass

    elif pilih == "Batu":
        if bot == "Batu":
            return "Draw !"
        elif bot == "Gunting":
            return "Anda Menang !"
        elif bot == "Kertas":
            return "Anda Kalah !"
        else :
            pass

    elif pilih == "Kertas":
        if bot == "Kertas":
            return "Draw !"
        if bot == "Batu":
            return "Anda Menang!"
        if bot == "Gunting":
            return "Anda Kalah !"
        else : 
            pass
    else:
        pass


def game (pilih):
    if pilih not in daftar:
        pass
    else:
        bot = random.choice(daftar) 
        print(f"\nBOT   = {bot}")
        print(f"Anda  = {pilih}\n")
        print(validasi_bot(pilih,bot))
        input("\n\nTekan Enter untuk coba lagi..")
        time.sleep(1)


#RUNNING
while True:
    os.system("clear")
    print(f"\n{'GAME GUNTING BATU KERTAS':^50}\n")
    game(input("Pilih [Gunting/Batu/Kertas]: ").title())
