'''5. Írjon programot jelszo.py néven, amely azt vizsgálja, hogy egy felhasználó helyesen adja-e meg a jelszavát! A program addig kérdezi újra a felhasználónév-jelszó párost, amíg a felhasználó mindkettőt hibátlanul meg nem adja. A program egyetlen felhasználó (bori99) jelszavát (Szivecske<3) ismeri, csak ezt a párost fogadja el helyesként. Mind a sikertelen, mind a sikeres bejelentkezési kísérletekről üzenetet ír a képernyőre.'''

felhasznalo = "bori99"
jelszo = "Szivecske<3"

a = 0
while a <= 0:
    felh_beirt = str(input("felhasználó: "))
    jelsz_beirt = str(input("jelszó: "))
    if felh_beirt == felhasznalo and jelsz_beirt == jelszo:
        a +=1
        break
    if felh_beirt is not felhasznalo and jelsz_beirt is not jelszo:
        print("sikertelen bejelentkezes")
        a = 0
print("bejelentkezve")