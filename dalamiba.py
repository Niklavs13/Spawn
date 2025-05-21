skaitlis = int(input("Ievadiet pirmo skaitli: "))
skaitlis2 = int(input("Ievadiet otro skaitli: "))
skaitlis3 = int(input("Ievadiet treso skaitli: "))
if skaitlis % 2 == 0 and skaitlis % 3 == 0:
    print("1. Skaitlis dalās gan ar 2 gan ar 3")
elif skaitlis % 2 == 0:
    print("1. Skaitlis dalās ar 2")
elif skaitlis % 3 == 0:
    print("1. Skaitlis dalās ar 3")
else:
    print("1. Skaitlis ne ar ko nedalās")
if skaitlis2 % 2 == 0 and skaitlis2 % 3 == 0:
    print("1. Skaitlis dalās gan ar 2 gan ar 3")
elif skaitlis2 % 2 == 0:
    print("2. Skaitlis dalās ar 2")
elif skaitlis2 % 2 == 0:
    print("2. Skaitlis dalās ar 3")
else:
    print("2. Skaitlis ne ar ko nedalās")
if skaitlis3 % 2 == 0 and skaitlis3 % 3 == 0:
    print("3. Skaitlis dalās gan ar 2 gan ar 3")
elif skaitlis3 % 2 == 0:
    print("3. Skaitlis dalās ar 2")
elif skaitlis3 % 2 == 0:
    print("3. Skaitlis dalās ar 3")
else:
    print("3. Skaitlis ne ar ko nedalās")