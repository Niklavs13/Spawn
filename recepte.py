print("Cepsim kūku!")
olas = int(input("Ievadiet olu skaitu: "))
cukurs = int(input("Ievadiet cukura skaitu gramos: "))
sviests = int(input("Ievadiet sviesta skaitu gramos: "))
milti = int(input("Ievadiet miltu skaitu gramos: "))
piens = int(input("Ievadiet piena daudzumu mililitros: "))
oluskaits = int(olas/4)
cukuraskaits = int(cukurs/150)
sviestaskaits = int(sviests/125)
miltuskaits = int(milti/115)
pienaskaits = int(piens/500)
mazakais = int(oluskaits)
if mazakais>cukuraskaits:
    mazakais = cukuraskaits
elif mazakais>sviestaskaits:
    mazakais = sviestaskaits
elif mazakais>miltuskaits:
    mazakais = miltuskaits
elif mazakais>pienaskaits:
    mazakais = pienaskaits
print("Jus varat uzcept ", mazakais," kūku")





