import random

min=0
max=100
adivinar=0
acertado=False

adivinar=random.randint(0,100)

respuesta=input(f"{adivinar} Es mayor, menor o igual que el numero que has pensado?")

while acertado==False:
    adivinar=random.randint(min,max)
    if respuesta=="Mayor":
        min=adivinar
        adivinar=random.randint(min,max)
    if respuesta=="Menor":
        max=adivinar
        adivinar=random.randint(min,max)
    if respuesta=="Igual":
        print(f"Soy un genio, tu numero es {adivinar}")
        acertado=True
    respuesta=input(f"{adivinar} Es mayor, menor o igual que el numero que has pensado?")