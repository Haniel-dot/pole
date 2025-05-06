cislo=[2,3,5,6,4,8]
hodn=int(input("zadejte cislo"))
for i in range(6):
    if hodn==cislo[i]:
        print(f"cislo je v poli",i)
    else:
        print("cislo neni v poli")