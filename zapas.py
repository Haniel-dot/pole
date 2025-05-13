skore=[]
for i in range(10):
    dalsi= int(input("zadejte skore hracu od 0 do 60"))
    skore.append(dalsi)
print(skore)
prumer=sum(skore)
print(prumer)
print(min(skore))
print(max(skore))
if prumer>250:
    print("Vyborny vykon")
else:
    print("Muzete to priste zkusit lepe")