# forca.py

import sys

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    letras_acertadas = ["_"] * len(palavra_secreta)
    letras_erradas = []
    print(letras_acertadas)
    while(not acertou and not enforcou):
        print("Jogando...")
        
        chute = input("Digite uma letra: ")

        if (len(chute) != 1 or not chute.isalpha()):
          print("Digite apenas uma letra!")
          break
        else:
          index = 0
          for letra in palavra_secreta:
              if (chute.upper == letra.upper):
                letras_acertadas[index] = letra
                print(f"Acertou a letra {chute}, na posição {index}")
              index += 1           
          print(letras_acertadas) 
          if "_" not in letras_acertadas:
                acertou = True
                print("Você descobriu a palavra!!!!")         
    print("Fim do jogo")

if (__name__ == "__main__"):
   jogar()