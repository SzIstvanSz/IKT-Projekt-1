"""1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!"""
"""1.2 Feladat
Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"""

def feladat1():
    text=input("Jó napod van?")

    if text=="Igen":
        print("Örülök neki!")
    elif text=="Nem":
        print("Ez szomorú...")
    else:
        print("Nem értem a választ.")
#feladat1()
"""2. Feladat
Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, hogy a megadott szám páros-e vagy páratlan!

[Tipp] A maradékos osztás segít! Mennyivel is kell elosztanod a számot maradékosan, hogy kiderüljön páros-e? Ebben az esetben mennyi lesz a maradék?"""



def feladat2():
    

    try:
        number=int(input("Kérem a számot!"))
        if number%2==0:
            print("A szám páros.")
        else:
            print("A szám páratlan.")
    except:
            print("Nem jó értéket adtál meg.")
#feladat2()

"""3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb."""

def feladat3():

    import random

    gondoltSzam=random.randrange(1,6)
    bekertSzam=int(input("Adj meg egy számot 1 és 5 között! "))
    if (0<bekertSzam<6):
        if (gondoltSzam>bekertSzam):
            print(f"A gép nagyobb számra gondolt: {gondoltSzam}")
        elif (gondoltSzam<bekertSzam):
            print(f"A gép kisebb számra gondolt: {gondoltSzam}")
        else:
            print(f"Eltaláltad a gép által gondolt számot! {gondoltSzam}")
    else:
        print("Nem jó értéket adtál meg.")

#feladat3()


def feladat4():
    try:
        gondoltSzam=random.randrange(1,6)
        bekertSzam=0

        while bekertSzam<1 or bekertSzam>5:
            bekertSzam=int(input("Adj meg egy számot 1 és 5 között! "))

        if (gondoltSzam>bekertSzam):
            print(f"A gép nagyobb számra gondolt: {gondoltSzam}")
        elif (gondoltSzam<bekertSzam):
            print(f"A gép kisebb számra gondolt: {gondoltSzam}")
        else:
            print(f"Eltaláltad a gép által gondolt számot! {gondoltSzam}")
    except:
        print("Nem jó értéket adtál meg.")

#feladat4()
"""Ciklusok:
A program minden alkalommal pontosan tájékoztassa a felhasználót, hogy mit kell tennie!

1. Feladat
Írj egy programot, amely kiírja a páros számokat 1 és 10 között!"""

def ciklus1():
    for i in range(1,11):
        if(i%2==0):
            print(i)

#ciklus1()

"""2. Feladat
Írj egy programot, amely csökkenő sorrendben írja ki a számokat 1 és 10 között!"""
def ciklus2():
    for i in reversed(range(1,11)):
        if(i%2==0):
            print(i)

#ciklus2()
"""3. Feladat
Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!"""
def ciklus3():
    for i in range(10,0,-1):
        if(i%2!=0):
            print(i)

#ciklus3()


"""4. Feladat
Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!"""
def ciklus4():
    number = int(input("Kérem az ismétlések számát!"))
    text = input("Kérem az ismétlődő szöveget!")

    for i in range(number):
        print(text)
ciklus4()




        
