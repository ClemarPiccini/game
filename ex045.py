# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('VAMOS JOGAR JOKENPO!!!')
print('''SUAS OPÇÕES
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada: '))
if jogador != 0 and jogador != 2 and jogador != 1:
    print('JOGADA INVALIDA!!!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-='*20)
    print('O computador escolheu {}'.format(itens[computador]))
    print('O jogador escolheu {}'.format(itens[jogador]))
    print('-='*20)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOOGADOR VENCE')
    elif computador == 2:
        if jogador == 0:
            print('JOGAOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
