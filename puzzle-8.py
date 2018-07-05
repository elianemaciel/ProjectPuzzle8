# -*- coding: utf-8 -*-

# grid = [[0, 1,3], [4, 2, 5], [7, 8, 6]]

import traceback

grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
BEST_DEPTH = 50

best_moves = []

lista_movimentos  = []

abort = 0

N = 3

resolvido = False

def display_board():
    print("-------------")
    print("| %i | %i | %i |" % (grid[0][0], grid[0][1], grid[0][2]))
    print("-------------")
    print("| %i | %i | %i |" % (grid[1][0], grid[1][1], grid[1][2]))
    print("-------------")
    print("| %i | %i | %i |" % (grid[2][0], grid[2][1], grid[2][2]))
    print("-------------")

def find(value):
    """Retorna linha e coluna da matriz"""
    if value < 0 or value > 8:
        raise Exception("value out of range")

    for row in range(3):
        try:
            col = grid[row].index(0)
            return row, col
        except:
            pass

def get_legal_moves(pos_x, pos_y, played_x, played_y):
    """Retorna lista de movimentos possíveis"""
    x1=pos_x+1
    y1=pos_y

    x2=pos_x-1
    y2=pos_y

    x3=pos_x
    y3=pos_y+1

    x4=pos_x
    y4=pos_y-1


    if(x1==played_x and y1==played_y):
        x1 = -1
        y1 = -1

    if(x2==played_x and y2==played_y):
        x2 = -1
        y2 = -1

    if(x3==played_x and y3==played_y):
        x3 = -1
        y3 = -1

    if(x4==played_x and y4==played_y):
        x4 = -1
        y4 = -1

    return x1, y1, x2, y2, x3, y3, x4, y4

def move(pos_x, pos_y, x1, y1):
    """Movimenta puzzle"""
    # get row and column of the empty piece
    grid[pos_x][pos_y]=grid[x1][y1]
    grid[x1][y1]=0

def valida():
    try:
        for row in range(3):
            for col in range(3):
                if not grid[row][col] == goal[row][col]:
                    return False
        return True
    except:
        print "Problema ao validar matriz"
        return False

def search_dfs(pos_x, pos_y, depth, played_x, played_y):
    global BEST_DEPTH, resolvido, abort

    if depth>=BEST_DEPTH:
        return

    if depth:
        lista_movimentos.insert(depth-1, grid[played_x][played_y])

    if valida():
        print("Solution found witch %d steps \n" % depth)
        print(grid)
        BEST_DEPTH=depth;
        resolvido = True
        for i in range(depth):
            best_moves.append(lista_movimentos[i])
        return

    x1, y1, x2, y2, x3, y3, x4, y4 = get_legal_moves(pos_x, pos_y, played_x, played_y)

    if (x1>=0) and (x1 < N) and (y1>=0) and (y1 < N):
        move(pos_x, pos_y, x1, y1)
        display_board()
        search_dfs(x1,y1, depth+1, pos_x,pos_y)
        move(x1, y1, pos_x, pos_y)
        if resolvido:
            return

    if (x2>=0) and (x2< N) and (y2>=0) and (y2 < N):
        move(pos_x, pos_y, x2, y2)
        display_board()
        search_dfs(x2, y2, depth+1, pos_x,pos_y)
        move(x2, y2, pos_x, pos_y)
        if resolvido:
            return

    if (x3>=0) and (x3 < N) and (y3>=0) and (y3 < N):
        move(pos_x, pos_y, x3, y3)
        display_board()
        search_dfs(x3, y3, depth+1, pos_x,pos_y)
        move(x3, y3, pos_x, pos_y)
        if resolvido:
            return

    if (x4>= 0) and (x4 < N) and (y4>=0) and (y4 < N):
        move(pos_x, pos_y, x4, y4)
        display_board()
        search_dfs(x4, y4, depth+1, pos_x,pos_y)
        move(x4, y4, pos_x,pos_y)
        if resolvido:
            return

    return

def main():
    global BEST_DEPTH
    matriz = raw_input("Digite os numeros da matriz, separados por espaços:\n")
    BEST_DEPTH = input("Digite o numero maximo de movimentos (maximo 50):\n")
    if BEST_DEPTH > 50:
        BEST_DEPTH = 50
    try:
        try:
            matriz = matriz.split()
            cont = 0
            for row in range(3):
                for col in range(3):
                    grid[row][col] = int(matriz[cont])
                    cont += 1

        except:
            print "Problema ao gerar matriz inicial " , traceback.print_exc()
            return

        if not valida():
            pos = find(0)
            if pos:
                search_dfs(pos[0], pos[1], 0, -1, -1)
                print(best_moves)
        else:
            print "O puzzle já está correto!!"

    except:
        print "Problema ao gerar a solução ", traceback.print_exc()



if __name__ == '__main__':
    main()
