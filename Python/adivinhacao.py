import random 
import sys  
print("**************")
print("Bem vindo ao teste")
print("**************")


numero_aleatorio = random.randint(1, 10)

erro1 = 0
tentativas = 1
nv_max = 3
nv_min = 1
try:
   nivel = int(input("Escolha o nivel de 1 à 3:"))
   if(nivel > nv_max or nivel < nv_min):
    print("Digite um numero entre o intervalo indicado.")
    sys.exit()
except ValueError:
   print("Por favor digite um numero inteiro.")
   sys.exit()
if(nivel == 1):
   total_tentativas = 5
elif(nivel == 2):
    total_tentativas = 3
else:
    total_tentativas = 1

while(tentativas <= total_tentativas):
    try:
        chute = int(input("Essa é a {} tentativa digite seu chute:".format(tentativas)))
    except ValueError:
       erro1 = 1
       print("Por favor digite um numero inteiro.") 
    acerto = chute == numero_aleatorio 
    maior = chute > numero_aleatorio 
    menor = chute < numero_aleatorio 

    if(erro1 == 1):
     print()
    else:
        if(acerto):
         print(f"Acertou!!na {tentativas}° tentativa")
         break
        elif(maior):
           print("Errou! você escolheu um numero maior")
        elif(menor):
           print("Errou! você escolheu um numero menor")
    tentativas += 1
print("FIM")
