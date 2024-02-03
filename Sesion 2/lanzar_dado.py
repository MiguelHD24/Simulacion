#lanzar dado

import random

lanzamientos = 0
cant_1 = 0
cant_2 = 0
cant_3 = 0
cant_4 = 0
cant_5 = 0
cant_6 = 0

while lanzamientos < 10:
    dado = random.randint(1,6)
    if dado == 1:
        cant_1 +=1
        print ("Numero 1")
    elif dado == 2:
        cant_2 +=1
        print("Numero 2")
    elif dado == 3:
        cant_3 +=1
        print("Numero 3")
    elif dado == 4:
        cant_4 +=1
        print("Numero 4")
    elif dado == 5:
        cant_5 +=1
        print("Numero 5")
    elif dado == 6:
        cant_6+=1
        print("Numero 6")
    
    lanzamientos += 1

porc_1 = (cant_1 / 10) * 100
porc_2 = (cant_2 / 10) * 100
porc_3 = (cant_3 / 10) * 100
porc_4 = (cant_4 / 10) * 100
porc_5 = (cant_5 / 10) * 100
porc_6 = (cant_6 / 10) * 100


print(f"Probabilidad de numero 1 {cant_1}%")
print(f"Probabilidad de numero 2 {cant_2}%")
print(f"Probabilidad de numero 3 {cant_3}%")
print(f"Probabilidad de numero 4 {cant_4}%")
print(f"Probabilidad de numero 5 {cant_5}%")
print(f"Probabilidad de numero 6 {cant_6}%")
