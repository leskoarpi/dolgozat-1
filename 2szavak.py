'''2. Írjon programot szavak.py néven! A program kérjen be két szót a felhasználótól, majd írja ki, hogy melyik a hosszabb!'''
a = str(input(" add meg az első szót: "))
b = str(input(" add meg a második szót: "))
if len(a)>len(b):
    print(a,"a hosszabb")
else:
    print(b, "a hosszabb")