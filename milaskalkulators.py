vards1 = input("Ievadiet pirmo vārdu")
vards2 = input("Ievadiet otro vārdu")
vards1 = vards1.lower()
vards2 = vards2.lower()

if vards1[-1]=="a" and vards2[-1]=="a" or vards1[-1]=="e" and vards2[-1]=="e" or vards1[-1]=="s" and vards2[-1]=="s":
    print("Saderība 0%")
else:
    if vards1.length==vards2.length:
        print("Saderība 100%")