import random
import time
import sys

posicaoDoUsuario = 1
jogadas = 0
decisaoUsuario = 0 

print("\nBem vindo, Guerreiros!")
time.sleep(0.5)
print("Seria a sua guilda capaz de atravessar nossa Dungeon?")
time.sleep(1.5)

while posicaoDoUsuario != 9 and (decisaoUsuario == 1 or decisaoUsuario == 2 or decisaoUsuario == 0):
 
    
    if posicaoDoUsuario != 10 and posicaoDoUsuario != 6:
        print("\nVocê esta sala {}".format(posicaoDoUsuario))
    elif posicaoDoUsuario == 10:
        posicaoDoUsuario = random.randint(1, 5)
        print("Oh no! Você caiu no buraco negro.")
        time.sleep(1.3)
        print("Teleportando para um lugar aleatorio",end="")
        time.sleep(0.6)
        print(".",end="")
        time.sleep(0.6)
        print(".",end="")
        time.sleep(0.6)
        print(".")
        time.sleep(1)
        print("")
        print("\nVocê esta na sala {}".format(posicaoDoUsuario))
    else:
        posicaoDoUsuario += 2
        print("Você caiu em um escorregador e acabou avançando mais duas salas!")
        print("Você esta na sala {}".format(posicaoDoUsuario))
    decisaoUsuario = int(input("Escolha seu caminho: \n[1]Caminho Vermelho \n[2]Caminho Preto\nMinha Escolha é: "))
    posicaoDoUsuario = posicaoDoUsuario + decisaoUsuario
    jogadas += 1
    
    
if jogadas >= 7:
    print("\nApesar dos guerreiros chegarem ao seu destino, todos morreram de cansaço!")
    print("\nVocê perdeu :(")
    sys.exit()
elif posicaoDoUsuario == 9:
    print("\nParabens, vocês chegaram ao final da Dungeon")
    sys.exit()
else:
    print("\nVocê não jogou corretamente, utilize apenas 1 ou 2. Favor reiniciar o game!")