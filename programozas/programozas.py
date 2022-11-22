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
feladat1()