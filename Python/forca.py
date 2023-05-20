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

#def jogar_forca():
    palavra_secreta = input("Digite a palavra secreta: ").lower()
    chances = 6
    letras_acertadas = []
    letras_erradas = []

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_acertadas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            letras_acertadas.append(letra)
        else:
            letras_erradas.append(letra)
            chances -= 1

        print("Palavra: ", end="")
        for caractere in palavra_secreta:
            if caractere in letras_acertadas:
                print(caractere, end=" ")
            else:
                print("_", end=" ")
        print("\n")

        print("Letras erradas:", letras_erradas)
        print("Chances restantes:", chances)
        print("\n")

        if len(letras_acertadas) == len(set(palavra_secreta)):
            print("Parabéns! Você acertou a palavra secreta:", palavra_secreta)
            break

        if chances == 0:
            print("Você perdeu! A palavra secreta era:", palavra_secreta)
            break

if (__name__ == "__main__"):
   jogar()