# -*- coding: utf-8 -*-


grid = [[0, 1,3], [4, 2, 5], [7, 8, 6]]

goal = [[0,1,2], [3,4,5], [6,7,8]]
BEST_DEPTH = 50

best_moves = []

lista_movimentos  = []

N = 3



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

def get_legal_moves(pos_zero, pos_x, pos_y):
    """Retorna lista de movimentos possíveis"""
    # get row and column of the empty piece
    # row, col = self.find(0)
    row, col = pos_x, pos_y
    free = []

    if row-1 == pos_x and col == pos_y:
        free.append((-1, -1))
    else:
        free.append((row - 1, col))
    if row  == pos_x and col-1 == pos_y:
        free.append((-1, -1))
    else:
        free.append((row, col - 1))
    if row+1 == pos_x and col == pos_y:
        free.append((-1, -1))
    else:
        free.append((row + 1, col))

    if row == pos_x and col+1 == pos_y:
        free.append((-1, -1))
    else:
        free.append((row, col + 1))
    # print free
    return free

def move(pos, pos_anterior):
    """Movimenta puzzle"""
    # get row and column of the empty piece
    row_ini, col_ini = pos_anterior[0], pos_anterior[1]
    aux = grid[pos[0]][pos[1]]
    grid[row_ini][col_ini] = aux
    grid[pos[0]][pos[1]] = 0

def valida():
    for row in range(3):
        for col in range(3):
            if not grid[row][col] == goal[row][col]:
                return False
    return True

def search_dfs(pos_x, pos_y, depth, played_x, played_y):
    global BEST_DEPTH
    # print grid
    # print "pos_x %d, pos_y %d, depth %d, played_x %d, played_y %d" % (pos_x, pos_y, depth, played_x, played_y)
    if depth>=BEST_DEPTH:
        # print BEST_DEPTH
        return

    if depth:
        lista_movimentos.insert(depth-1, grid[played_x][played_y])

    if valida():
        print("Solution found witch %d steps \n" % depth)
        print(grid)
        BEST_DEPTH=depth;
        for i in range(depth):
            best_moves.append(lista_movimentos[i])
        return

    # moves = get_legal_moves(pos_zero, played_x, played_y)
    x1=0
    y1=0
    y2=0
    x2=0
    x3=0
    y3=0
    x4=0
    y4=0

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

    # print moves
    if (x1>=0)  and (x1 < N) and (y1>=0) and (y1 < N):
        # move((x1,y1), pos_zero)
        grid[pos_x][pos_y]=grid[x1][y1]
        grid[x1][y1]=0
        # print "RECURSAO"
        search_dfs(x1,y1, depth+1, pos_x,pos_y)
        grid[x1][y1]=grid[pos_x][pos_y]
        grid[pos_x][pos_y]=0


    if (x2>=0) and (x2< N) and (y2>=0) and (y2 < N):
        grid[pos_x][pos_y]=grid[x2][y2]
        grid[x2][y2]=0
        # print "RECURSAO"
        search_dfs(x2, y2, depth+1, pos_x,pos_y)
        grid[x2][y2]=grid[pos_x][pos_y]
        grid[pos_x][pos_y]=0

    if (x3>=0) and (x3 < N) and (y3>=0) and (y3 < N):
        grid[pos_x][pos_y]=grid[x3][y3]

        grid[x3][y3]=0
        # print "RECURSAO"
        search_dfs(x3, y3, depth+1, pos_x,pos_y)
        grid[x3][y3]=grid[pos_x][pos_y]
        grid[pos_x][pos_y]=0

    if (x4>= 0) and (x4 < N) and (y4>=0) and (y4 < N):
        grid[pos_x][pos_y]=grid[x4][y4]
        grid[x4][y4]=0
        # print "RECURSAO"
        search_dfs(x4, y4, depth+1, pos_x,pos_y)
        grid[x4][y4]=grid[pos_x][pos_y]
        grid[pos_x][pos_y]=0

    return

def main():
    global BEST_DEPTH
    # puzzle = Puzzle()
    # puzzle.maximo = 800
    pos = find(0)
    if not valida():
        print("ok")
    search_dfs(pos[0], pos[1], 0, -1, -1)
    print(best_moves)
    return


if __name__ == '__main__':
    main()
