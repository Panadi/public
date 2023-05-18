# adivinhacao.py

import random 
import sys

def jogar():
    print("**************")
    print("Bem vindo ao jogo de adivinhação!!!")
    print("**************")


    numero_aleatorio = random.randint(1, 100)
    erro1 = 0
    nv_max = 3
    nv_min = 1
    pontos_iniciais = 1000

    def adivinhacao(total_tentativas, pontos_iniciais):
        tentativas = 1
        pontos = pontos_iniciais
        while(tentativas <= total_tentativas):
            
            erro1 = 0
            try:
                chute = int(input("Essa é a {} tentativa digite seu chute:".format(tentativas)))
                if (chute <= 0 or chute > 100):
                 print("escolha o valor entre 1 e 100")
                
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
              print(f"Acertou!!na {tentativas}° tentativa e fez {pontos} pontos")
              break
             elif(maior):
              print("Errou! você escolheu um numero maior.")
             elif(menor):
              print("Errou! você escolheu um numero menor.")
            tentativas += 1
            pontos_perdidos = abs(numero_aleatorio - chute)
            pontos = pontos - pontos_perdidos                        
                
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
    adivinhacao(total_tentativas, pontos_iniciais)
    print("FIM")
