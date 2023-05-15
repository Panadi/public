import random 
import sys  
print("**************")
print("Bem vindo ao teste")
print("**************")


numero_aleatorio = random.randint(1, 10)
erro1 = 0
nv_max = 3
nv_min = 1
pontuacao = 1000

def adivinhacao(total_tentativas, pontuacao):
    tentativas = 1
    while(tentativas <= total_tentativas):
        erro1 = 0
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
          print(f"Acertou!!na {tentativas}° tentativa.")
          break
         elif(maior):
           print("Errou! você escolheu um numero maior.")
           pontuacao -= 10
         elif(menor):
           print("Errou! você escolheu um numero menor.")
           pontuacao -= 10
        tentativas += 1
        return pontuacao
def nivel():
    try:
        nivel = int(input("Escolha o nivel de 1 à 3:"))
        if(nivel > nv_max or nivel < nv_min):
            print("Digite um numero entre o intervalo indicado.")
            sys.exit()
    except ValueError:
        print("Por favor digite um numero inteiro.")
        sys.exit()
    return nivel
   
def chances(nivel):
   total_tentativas = int((5/nivel)*2)
   return total_tentativas

total_tentativas = chances(nivel())
adivinhacao(total_tentativas,pontuacao)
pontuacao_final = adivinhacao(total_tentativas, pontuacao)
print("Sua pontuação final é: ", pontuacao_final)
print("FIM")