#lanzar moneda

import random

lanzamientos = 0
cant_num = 0
cant_escudo = 0

while lanzamientos < 10:
    moneda = random.randint(0,1)
    if moneda == 0:
        cant_escudo+=1
        print ("escudo")
    else:
        cant_num +=1
        print("numero")
    lanzamientos += 1

porc_num = (cant_num / 10) * 100
porc_esc = (cant_escudo / 10) * 100

print(f"Probabilidad de escud {porc_esc}%")
print(f"Probabilidad de numero {porc_num}%")