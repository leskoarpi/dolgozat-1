'''3. Egy bolt pontban reggel nyolc órakor nyit, és pontban délután tizenhat órakor zár be – azaz 8:00-kor márnyitva van és 16:00-kor már nincs nyitva.Írjon programot nyitvatartas.py néven! A program kérjen be egy egész órát jelző számot a felhasználótól,majd írja ki, hogy a megadott időpontban nyitva van-e a bolt! Amennyiben igen, akkor azt is írja ki, hogymennyi idő van még zárásig, azaz hány egész óra áll rendelkezésre odaérni a boltba'''
a = int(input('add meg az idöpontot: '))  
if a >= 16 or a < 8:
    print('zárva')
elif a < 16 or a > 8:
    print("nyitva,", 16 - a,"óra van még zárásig")