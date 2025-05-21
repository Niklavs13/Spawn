stunda = int(input("Ievadiet stundu skaitu "))
minute = int(input("Ievadiet minūšu skaitu "))
if stunda < 24 and stunda > -1 and minute < 60 and minute > -1:
    print("Laiks ir derīgs")
else:
    print("Laiks ir nederīgs")
    