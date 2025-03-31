"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""

tartalom = []
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        csapat = adatok[1]
        gyozelmek = int(adatok[2])
        futamok = int(adatok[3])
        # formaegy = {'név': adatok[0], 'csapat': adatok[1], 'győzelmek': int(adatok[2]), 'futamok': int(adatok[3])}
        tartalom.append([nev, csapat, gyozelmek, futamok])
        

# print(f'{tartalom=}')
print(f"A beolvasott fájlban összesen {len(tartalom)} versenyző szerepel.")

legtobb_futamgyozelem = 0
legtobb_futamgyozelmu_versenyzo = None
for versenyzok in tartalom:
    if versenyzok[2] > legtobb_futamgyozelem:
        legtobb_futamgyozelem = versenyzok[2]
        legtobb_futamgyozelmu_versenyzo = versenyzok
        
    
# print(legtobb_futamgyozelem)
# print(legtobb_futamgyozelmu_versenyzo)

print(f"A legtöbb futamot nyert versenyző: {legtobb_futamgyozelmu_versenyzo[0]} ")

legtobb_futamu_versenyzo = 0
for versenyzo in tartalom:
    if versenyzok[3] >legtobb_futamu_versenyzo:
        legtobb_futamu_versenyzo = versenyzok[3]



print(f"A legtöbb futamot teljesített versenyző: {legtobb_futamgyozelmu_versenyzo[0]}")

futamok_szama = 0
for versenyzo in tartalom:
    futamok_szama += versenyzok[3]

atlagos_futamszam = futamok_szama / len(tartalom)
# print(futamok_szama)
# print(atlagos_futamszam)
print(f"Az átlagos futamszám: {atlagos_futamszam}")

with open('kiirt_adatok.txt', 'w', encoding='utf-8') as celfajl:
    print(f"A beolvasott fájlban összesen {len(tartalom)} versenyző szerepel.", file=celfajl)
    print(f"A legtöbb futamot nyert versenyző: {legtobb_futamgyozelmu_versenyzo[0]}", file=celfajl)
    print(f"A legtöbb futamot teljesített versenyző: {legtobb_futamgyozelmu_versenyzo[0]}", file=celfajl)
    print(f"Az átlagos futamszám: {atlagos_futamszam}", file=celfajl)