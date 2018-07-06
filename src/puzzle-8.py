# -*- coding: utf-8 -*-

__author__ = "Eliane Maciel e Maria Carolina"

import traceback
# Matriz inicial
init =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Matriz do puzzle
puzzle = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Matriz certa
goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Número maximo de movimetos
BEST_DEPTH = 50

# Melhores movimentos
best_moves = []

# lista de todos os moniventos
lista_movimentos  = []

# Tamanho da matriz 3*3
N = 3

# Flag para ver se encontrou solução
RESOLVIDO = False


def display_board():
    """Printa a matriz"""

    print("-------------")
    print("| %i | %i | %i |" % (puzzle[0][0], puzzle[0][1], puzzle[0][2]))
    print("-------------")
    print("| %i | %i | %i |" % (puzzle[1][0], puzzle[1][1], puzzle[1][2]))
    print("-------------")
    print("| %i | %i | %i |" % (puzzle[2][0], puzzle[2][1], puzzle[2][2]))
    print("-------------")

def printMoviments(p):
    """Printa a matriz"""

    pp = p
    rowz = 0
    colz = 0
    rown = 0
    coln = 0
    cont = 0
    print("Puzzle inicial")
    print("-------------")
    print("| %i | %i | %i |" % (pp[0][0], pp[0][1], pp[0][2]))
    print("-------------")
    print("| %i | %i | %i |" % (pp[1][0], pp[1][1], pp[1][2]))
    print("-------------")
    print("| %i | %i | %i |" % (pp[2][0], pp[2][1], pp[2][2]))
    print("-------------")
    for num in best_moves:
        cont += 1
        for row in range(N):
            try:
                col = pp[row].index(0)
                rowz = row
                colz = col
            except:
                pass
        for row in range(N):
            try:
                col = pp[row].index(num)
                rown = row
                coln = col
            except:
                pass
        pp[rown][coln] = 0
        pp[rowz][colz] = num

        print("Moveu o ",num," index: ",cont )
        print("-------------")
        print("| %i | %i | %i |" % (pp[0][0], pp[0][1], pp[0][2]))
        print("-------------")
        print("| %i | %i | %i |" % (pp[1][0], pp[1][1], pp[1][2]))
        print("-------------")
        print("| %i | %i | %i |" % (pp[2][0], pp[2][1], pp[2][2]))
        print("-------------")


def find(value):
    """Retorna linha e coluna onde tem o 0 na matriz"""

    if value < 0 or value > 8:
        raise Exception("Valor errado")

    for row in range(N):
        try:
            col = puzzle[row].index(0)
            return row, col
        except:
            pass


def get_legal_moves(pos_x, pos_y, played_x, played_y):
    """
    Retorna lista de movimentos possíveis.
    @param: int pos_x, int pos_y, (posicao atual),
        int played_x, int played_y (posicao anterior)
    @return: int mov_x1, mov_y1, mov_x2, mov_y2, mov_x3, mov_y3, mov_x4, mov_y4 (movimentos possiveis)
    """

    mov_x1 = pos_x + 1
    mov_y1 = pos_y

    mov_x2 = pos_x - 1
    mov_y2 = pos_y

    mov_x3 = pos_x
    mov_y3 = pos_y + 1

    mov_x4 = pos_x
    mov_y4 = pos_y-1


    if mov_x1 == played_x and mov_y1 == played_y:
        mov_x1 = -1
        mov_y1 = -1

    if mov_x2 == played_x and mov_y2 == played_y:
        mov_x2 = -1
        mov_y2 = -1

    if mov_x3 == played_x and mov_y3 == played_y:
        mov_x3 = -1
        mov_y3 = -1

    if mov_x4 == played_x and mov_y4 == played_y:
        mov_x4 = -1
        mov_y4 = -1

    return mov_x1, mov_y1, mov_x2, mov_y2, mov_x3, mov_y3, mov_x4, mov_y4


def move(pos_x, pos_y, x1, y1):
    """
    Movimenta puzzle
    @param: int pos_x, int pos_y (posicao atual)
        int x1, int y1 (posicao que muda)
    """

    puzzle[pos_x][pos_y]=puzzle[x1][y1]
    puzzle[x1][y1]=0


def valida():
    """
    Verifica se a matriz está correta.
    @return: True or False
    """

    try:
        for row in range(N):
            for col in range(N):
                if not puzzle[row][col] == goal[row][col]:
                    return False
        return True
    except:
        print("Problema ao validar matriz")
        return False


def solver_dfs(pos_x, pos_y, depth, played_x, played_y):
    """
    Verifica se a matriz está correta.
    @param: int pos_x, pos_y (Posicao 0 atual) depth (profundidade), played_x, played_y (posicao anterior)
    """

    global BEST_DEPTH, RESOLVIDO  # Variáveis globais

    if depth >= BEST_DEPTH:
        return

    if depth:
        lista_movimentos.insert(depth-1, puzzle[played_x][played_y])

    if valida():
        print("Solução encontrada %d passos \n" % depth)
        BEST_DEPTH = depth
        RESOLVIDO = True
        for i in range(depth):
            best_moves.append(lista_movimentos[i])
        return

    x1, y1, x2, y2, x3, y3, x4, y4 = get_legal_moves(pos_x, pos_y, played_x, played_y)

    if (x1 >= 0) and (x1 < N) and (y1 >= 0) and (y1 < N):
        move(pos_x, pos_y, x1, y1)
        solver_dfs(x1, y1, depth + 1, pos_x, pos_y)
        if RESOLVIDO:
            return
        move(x1, y1, pos_x, pos_y)


    if (x2 >= 0) and (x2 < N) and (y2 >= 0) and (y2 < N):
        move(pos_x, pos_y, x2, y2)
        solver_dfs(x2, y2, depth + 1, pos_x, pos_y)
        if RESOLVIDO:
            return
        move(x2, y2, pos_x, pos_y)


    if (x3 >= 0) and (x3 < N) and (y3 >= 0) and (y3 < N):
        move(pos_x, pos_y, x3, y3)
        solver_dfs(x3, y3, depth + 1, pos_x, pos_y)
        if RESOLVIDO:
            return
        move(x3, y3, pos_x, pos_y)


    if (x4 >= 0) and (x4 < N) and (y4 >= 0) and (y4 < N):
        move(pos_x, pos_y, x4, y4)
        solver_dfs(x4, y4, depth + 1, pos_x, pos_y)
        if RESOLVIDO:
            return
        move(x4, y4, pos_x, pos_y)

    return


def main():
    """Resolvedor do Puzzle 8"""

    global BEST_DEPTH

    matriz = input("Digite os numeros da matriz, separados por espaços:\n")
    BEST_DEPTH = int(input("Digite o numero maximo de movimentos (maximo 50):\n"))

    if BEST_DEPTH > 50:
        BEST_DEPTH = 50
    try:
        try:
            matriz = matriz.split()
            cont = 0
            for row in range(N):
                for col in range(N):
                    puzzle[row][col] = int(matriz[cont])
                    init[row][col] = int(matriz[cont])
                    cont += 1
        except:
            print("Problema ao gerar matriz inicial " , traceback.print_exc())
            return

        if not valida():
            pos = find(0)
            if pos:
                solver_dfs(pos[0], pos[1], 0, -1, -1)
                if best_moves:
                    print("Melhores Movimentos: {moves}".format(moves=best_moves))
                    print("Caminhos:")
                    printMoviments(init)
                else:
                    print("Não foi possivel encontrar a solução para o puzzle com esses movimentos")
                print("Movimentos realizados: {mov}".format(mov=len(lista_movimentos)))
                display_board()
        else:
            print("O puzzle já está correto!!")
    except:
        print("Problema ao gerar a solução ", traceback.print_exc())


if __name__ == '__main__':
    main()
