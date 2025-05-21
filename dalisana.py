skaitlis = int(input("Ievadiet pirmo skaitli: "))
skaitlis2 = int(input("Ievadiet otro skaitli: "))
if skaitlis2 == 0:
    print("Skaitlis ir nulle")
else:

    vesels = skaitlis // skaitlis2
    atlikums = skaitlis % skaitlis2
    print("Dalijums ir ",vesels, " atlikums ir: ",atlikums)