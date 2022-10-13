""" For loops """

for i in range(5): # 0,1,2,3,4
    print(i, end=",")
    


liste_1 = [2, 7, 5, 2, 9, 4, 0, 5]

listeUzunluk = len(liste_1)
print(listeUzunluk)


for listeElemani in liste_1:
    print(listeElemani, end=", ")
    
    
for i in range(100, 49, -2):
    print(i)
    

kelimeler = ["kedi", "köpek", "balık", "kuş"]

for i in kelimeler:
    print(i, len(i))
    



kullanıcılar = {"Ali" : 35,
                "Mehmet" : 40,
                "Tarık" : 45}

print(kullanıcılar)

for x, y in kullanıcılar.copy().items():
    if y == 45:
        del kullanıcılar[x]

print(kullanıcılar)




for k in range(10, 15, 1):
    print(k)



bosListe= []

for i in range(5): # 0, 1, 2, 3, 4
    for k in range(5): # 0, 1, 2, 3, 4
        x = i, k
    
        bosListe.append(x)

print(bosListe)

print(len(bosListe))


































