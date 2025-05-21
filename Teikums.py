# teikums = (int
teikums = "Jauka diena ir pirmdiena."
print("1. uzdemums ",len(teikums))
print("2. uzdemums ", teikums[0])
print("3. uzdemums ",teikums[-2])
aA_skaits = teikums.count("a") + teikums.count("A")
print("4. uzdevums ", aA_skaits)
atstarpes_skaits = teikums.count(" ")
print("5. uzdevums ", atstarpes_skaits)
varda_beigas = teikums.find(" ")
for i in range(varda_beigas):
    print(teikums[i], end="")
print("7. uzdevums - pedejais vards")
for i in range (-2,0,-1):
    if teikums[i] == " ":
        pedeja_atstarpe = i
        break
# print(pedeja_atstarpe)
simb_skaits = len(teikums)
print(simb_skaits+pedeja_atstarpe-1)
for i in range (simb_skaits+pedeja_atstarpe-1 )

