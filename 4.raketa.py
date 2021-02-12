'''4. Egy rakéta indítása előtt több órával visszaszámlálást kezdenek és óránként egyet számolnak vissza a rakéta indításáig. A felhasználó határozza meg, hogy hány órás a visszaszámlálás. A visszaszámlálást minden órában egy órára felfüggeszthetik, ha valamilyen váratlan esemény – műszaki hiba, időjárási probléma – merül fel. Amikor a visszaszámlálás eléri a 0-t, a rakétát fellövik. Írjon programot raketa.py néven, amely a visszaszámlálás számait jeleníti meg a képernyőn! Természetesen nem kell a visszaszámlálás lépései között eltelni időnek – minden üzenet megjelenését azonnal követheti a következő. A visszaszámlálás minden lépésénél kérdezze meg a felhasználót, hogy az adott órában szükség volt-e a visszaszámlálás fölfüggesztésére! A visszaszámlálás megjelenítését követően a program írja ki, hogy a visszaszámlálás kezdetétől hány óra telt el – a visszaszámlálás eredetileg tervezett hosszát a felfüggesztésekkel megnövelve!'''
from time import sleep

visszaszámlálás = 10
eltelt_ido = 10
while visszaszámlálás != 0:
    print(visszaszámlálás)
    visszaszámlálás -= 1
    valasz = str(input("volt szükség karbantartásra? (i/n): "))
    if valasz == str("i"):
        eltelt_ido +=1
        sleep(1)

print("fellövés!")
print("összesen",eltelt_ido,"óra telt el fellövésig")