# forca.py

import sys

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        print("Jogando...")
        while True:
         chute = input("Digite uma letra: ")
         if len(chute) != 1 or not chute.isalpha():
          print("Digite apenas uma letra!")
          sys.exit()
         

    print("Fim do jogo")


if (__name__ == "__main__"):
   jogar()