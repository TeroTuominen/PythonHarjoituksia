sana = str(input("Sana:"))
raamit = 30
tyhjätväli = raamit - len(sana) -2
vasen_tyhjä = tyhjätväli // 2
oikea_tyhja = tyhjätväli - vasen_tyhjä
print("*"*raamit)
print('*'+ ' '*vasen_tyhjä + sana + " "*oikea_tyhja + "*")
print("*"*raamit)

print(len(sana))
print(2/2)