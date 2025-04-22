#vytvareni  pole
skola = ["jídelna", "učebny", "kamarádi", "nuda", "fyzika", "matematika"]

#vysani pocet hodnot
print(len(skola))

#cyklus pro pole
for i in skola:
    print(i)

#pridani od uzivatele
dalsi= input("zadejte dalsi predmet")
skola.append(dalsi)

#odstraneni
skola.remove("učebny")

#seradit
print(skola.sort)

#obratit poradi
print(skola.reverse)

