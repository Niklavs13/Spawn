import random
slepenais = random.randint(1,10))
gajienu_skaits = 0
while(True):
    if max_minejumi == gajienu_skaits:
        print("Nepaspeji uzminet, beigas!")
        break
    print("Ievadi skaitli")
    skaitlis = int(input))
    gajienu_skaits +=1
    max_minejumi = 5
    if skaitlis == slepenais:
        print("Uzminēji!")
        break
    if skaitlis>slepenais:
        print("Skaitlis ir par lielu")
        break
    if skaitlis<slepenais:
        print("Skaitlis ir par mazu!")
        break
