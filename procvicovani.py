ovoce=["jablko","banán","pomeranč","kiwi","hruška"]
 
#Napsat co vypise
print(ovoce[0]) #jablko
print(ovoce[2]) #pomeranč
print(ovoce[-1]) #hruška
print("--------------------")
 
#oblibene jidlo
jidlo=["kobliha","jogurt","mango"]
print(jidlo)
print("--------------------")
 
#znamky
cestina=[1,2,1,1,5]
soucet=sum(cestina)
print(f"soucet znamek je ",soucet)
pocet=len(cestina)
print(f"je tam ",pocet, "znamek")
for i in cestina:
    print(i)
print("--------------------")
 
#zvirata
zvirata=["kocka","slepice","panda","krava"]
print(zvirata[1])
print(zvirata[-1])
print("--------------------")
 
#prazdny seznam
seznam=[]
for i in range(3):
    seznam.append(input())
print(seznam)
print("--------------------")
 
#filmy
filmy=["ptaci","cupa mia","scream"]
for i in filmy:
    print(i)
print("--------------------")
 
#seznam cisel
cisla=[1,25,96]
cisla[1]=999
print(cisla)
print("--------------------")
 
#libove cislo
libova=[1,5,95,6,87]
soucet=sum(libova)
print(f"soucet cisel je ",soucet)
print("--------------------")
 
#libove pole
pole=["Míša","Nelča","Týna","Hanča"]
print(f"velikost pole je",len(pole))
print("--------------------")
 
#aritmeticky prumer
aritznamky=[1,3,5,4,2,4,3]
soucet=sum(aritznamky)
arit=soucet/len(aritznamky)
print(arit)
print("--------------------")
 
#seznam ovoce
sezovoce=["jahody","pomerance","ananas","banan"]
for i in sezovoce:
    if i=="banan":
        print("banan tam je")
print("--------------------")
 
 