import random   
print("**************")
print("Bem vindo ao teste")
print("**************")

erro1 = 0
numero_aleatorio = random.randint(1, 10)
try:
    chute = int(input("digite seu chute:"))
except ValueError:
    erro1 = 1
    print("Por favor digite um numero inteiro.")

if(erro1 == 1):
   print()
else:
    if(numero_aleatorio == chute):
     print("Acertou!!")

    else:
     print("Errou! O numero é "+ str(numero_aleatorio))

print("FIM")
