'''1. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a

legkisebb értéket ezek közül!'''
'''
szam1 = int(input('Add meg az 1. számot '))
szam2 = int(input('Add meg a 2. számot '))
szam3 = int(input('Add meg a 3. számot '))

if szam1 < szam2 and szam1 < szam3: print("A legkisebb szám: ", szam1)
if szam2 < szam1 and szam2 < szam3: print("A legkisebb szám: ", szam2)
if szam3 < szam1 and szam3 < szam2: print("A legkisebb szám: ", szam3)

#vagy

def feladat1():
    tomb =[]

    for i in range(3):
        tomb.append(int(input("Kérek egy számot")))


    print("A legkisebb szám: ",min(tomb))

feladat1()'''
'''2. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a

legnagyobb értéket ezek közül!'''
'''
szam1 = int(input('Add meg az 1. számot '))
szam2 = int(input('Add meg a 2. számot '))
szam3 = int(input('Add meg a 3. számot '))

if szam1 > szam2 and szam1 > szam3: print("A legnagyobb szám: ", szam1)
if szam2 > szam1 and szam2 > szam3: print("A legnagyobb szám: ", szam2)
if szam3 > szam1 and szam3 > szam2: print("A legnagyobb szám: ", szam3)
'''

def feladat2():
    tomb =[]

    for i in range(3):
        tomb.append(int(input("Kérek egy számot ")))


    print("A legnagyobb szám: ", max(tomb))

feladat2()

'''3. Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.'''

pont = int(input("Add meg a pontszámot!"))

if pont < 50: print("Egyes")
if pont >= 50 and pont < 60: print("Kettes")
if pont >= 60 and pont < 70: print("Hármas")
if pont >= 70 and pont < 85: print("Négyes")
if pont >= 85 and pont < 100: print("Ötös")

'''4. Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre, hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!'''
szam = int(input('Adj meg egy egész számot! '))
if szam % 3 == 0: print("A szám osztható hárommal.")
if szam % 5 == 0: print("A szám osztható öttel.")
else:
        print("A szám nem osztható sem hárommal sem öttel.")

'''5. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre, hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!'''


'''6. Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a képernyőre, hogy mind a három páros szám-e (igen/nem)!'''


'''7. Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól és ABC sorrendben kiírja őket a képernyőre!'''


'''8. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a

képernyőre azokat a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!
'''

'''9. Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a

képernyőre azokat a páros számokat, amelyek a két adott érték közötti zárt intervallumban

találhatóak!'''


'''10. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a

felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi

a megadott szám értéke!'''