
tabela = [1, 2, 3,
          4, 5, 6,
          7, 8, 9]


def alinhar():
    print(tabela[0], '|', tabela[1], '|', tabela[2])
    print('-' * 9)
    print(tabela[3], '|', tabela[4], '|', tabela[5])
    print('-' * 9)
    print(tabela[6], '|', tabela[7], '|', tabela[8])

turno = 0


def player1():
    while True:
        posicao = int(input('Escolha a posição jogador 1:'))
        while int(posicao) < 1 or int(posicao) > 9 :
            posicao = input('Escolha a posição jogador 1:')
        n = int(posicao)
        n -= 1
        if tabela[n] == 'X' or tabela[n] == 'O':
            print('Posiçao inválida')
            continue
        else:
            break
    tabela[n] = 'X'
    print(f'turno: ', turno)
    alinhar()

alinhar()


def player2():
    while True:
        posicao = input('Escolha a posição jogador 2:')
        while int(posicao) < 1 or int(posicao) > 9:
            posicao = input('Escolha a posição jogador 2:')
        n = int(posicao)
        n -= 1
        if tabela[n] == 'X' or tabela[n] == 'O':
            print('Posiçao inválida')
            continue
        else:
            break
    tabela[n] = 'O'
    print(f'turno: ', turno)
    alinhar()

tabela = ['-', '-', '-',
          '-', '-', '-',
          '-', '-', '-']


def ganhou(turnos):
    if (
            # Avaliando as linhas
            (tabela[0] == turnos and tabela[1] == turnos and tabela[2] == turnos) or
            (tabela[3] == turnos and tabela[4] == turnos and tabela[5] == turnos) or
            (tabela[6] == turnos and tabela[7] == turnos and tabela[8] == turnos) or

            # Avaliando as colunas
            (tabela[0] == turnos and tabela[3] == turnos and tabela[6] == turnos) or
            (tabela[1] == turnos and tabela[4] == turnos and tabela[7] == turnos) or
            (tabela[2] == turnos and tabela[5] == turnos and tabela[8] == turnos) or

            # Avaliando as diagonais
            (tabela[0] == turnos and tabela[4] == turnos and tabela[8] == turnos) or
            (tabela[2] == turnos and tabela[4] == turnos and tabela[6] == turnos)
    ):
        return True
    else:
        return False

turnoplayer1 = True
for i in range(0, 9):
    if turnoplayer1:
        player1()
        turno += 1

        if ganhou('X'):
            print('Jogador 1 ganhou')
            break
        else:
            player2()
            turno += 1
            if ganhou('O'):

                print('Jogador 2 ganhou')
                break

    turnoplayer1 = not turnoplayer1

    if i == 8:
        print('Deu velha')
        print('Fim do jogo.')
        break
