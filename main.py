from baralho import Baralho
from jogadores import Jogador
import random

def main():
    print('Bem vindo ao jogo de Blackjack')
    b = Baralho()
    global baralho
    baralho = b.baralho
    random.shuffle(baralho)
    global jogador
    jogador = Jogador()
    global banca
    banca = Jogador()

    while jogador.soma < 21 and banca.soma < 21:
        opcao = input('>> Digite "s" para tirar uma carta e "n" para parar: ')
        print()
        if opcao == 's':
            if banca.soma < 17:
                vez_do_jogador(opcao)
                vez_da_banca()
            else:
                vez_do_jogador()
                print('A banca parou')
        elif opcao == 'n':
            while banca.soma < 17:
                vez_da_banca()
            break
        else:
            print('Opção inválida')
            print()

    if jogador.soma > 21:
        print('Vitória da banca!')
    elif banca.soma > 21:
        print('Parabéns! Você ganhou!')
    elif jogador.soma > banca.soma:
        print('Parabéns! Você ganhou!')
    elif jogador.soma < banca.soma:
        print('Vitória da banca!')
    else:
        print('Empate!')

    opcao = input('Deseja jogar de novo? s/n ')
    print()
    if opcao == 's':
        main()
    else:
        print('Volte sempre!')
        exit()

def tirar_carta():
    carta = baralho[0]
    print('Sua carta é:', carta)
    print()
    if carta[0] == 1:
        valor = 11
    elif carta[0] < 10:
        valor = carta[0]
    else:
        valor = 10
    baralho.remove(baralho[0])

    return valor


def vez_do_jogador(opcao):
    print('Vez do jogador')
    total = tirar_carta()
    jogador.soma += total


def vez_da_banca():
    print('Vez da banca')
    total = tirar_carta()
    banca.soma += total

if __name__ == '__main__':
    main()