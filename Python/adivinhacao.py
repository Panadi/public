import random   
print("**************")
print("Bem vindo ao teste")
print("**************")
tentativas = 0
erro1 = 0
numero_aleatorio = random.randint(1, 10)

while(tentativas <= 4):
    try:
        chute = int(input("digite seu chute:"))
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
         print("Acertou!!")
         break
        elif(maior):
           print("Errou! você escolheu um numero maior")
        elif(menor):
           print("Errou! você escolheu um numero menor")
    tentativas += 1
print("FIM")
