# -*- coding: utf-8 -*-


goal_state = [[1,3, 2],
            [8,0,4],
            [7,6, 5]]

BEST_DEPTH = 50

best_moves = []

lista_movimentos  = []

N = 3

class Puzzle:

    def __init__(self):
        self.adj_matrix = []
        self.lista_posicoes = []
        self.pos_anterior = ()
        self.linha1 = False
        for i in range(3):
            self.adj_matrix.append(goal_state[i][:])

    def find(self, value):
        """Retorna linha e coluna da matriz"""
        if value < 0 or value > 8:
            raise Exception("value out of range")

        for row in range(3):
            try:
                col = self.adj_matrix[row].index(0)
                return row, col
            except:
                pass

    def get_legal_moves(self, pos_zero, pos_x, pos_y):
        """Retorna lista de movimentos possíveis"""
        # get row and column of the empty piece
        # row, col = self.find(0)
        row, col = pos_zero[0], pos_zero[1]
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

    def move(self, pos, pos_anterior):
        """Movimenta puzzle"""
        # get row and column of the empty piece
        row_ini, col_ini = pos_anterior[0], pos_anterior[1]
        aux = self.adj_matrix[pos[0]][pos[1]]
        self.adj_matrix[row_ini][col_ini] = aux
        self.adj_matrix[pos[0]][pos[1]] = 0
        self.pos_anterior = (row_ini, col_ini)

    def valida(self):
        n = 0
        for row in range(3):
            for col in range(3):
                n = n + 1 if n < 8 else 0
                if not self.adj_matrix[row][col] == n:
                    return False
            self.linha1 = True
        return True    

def back(pos, puzzle, n):
    pass
    # print puzzle.adj_matrix
    # if puzzle.valida():
    #     print puzzle.adj_matrix
    #     return
    # else:
    #     moves = puzzle.get_legal_moves()
    #     print moves
    #     moves

    #         if  not move == puzzle.pos_anterior:
    #             print "MOVE", move
    #             puzzle.move(move)
    #     if n < puzzle.maximo:
    #         back(puzzle.find(0), puzzle, n+1)
    #     else:
    #         return


def search_dfs(puzzle, pos_zero, depth, played_x, played_y):
    global BEST_DEPTH, best_moves, lista_movimentos

    if(depth>=BEST_DEPTH):
        return
    
    if(depth!=0):

        lista_movimentos.insert(depth-1, puzzle.adj_matrix[played_x][played_y])
    
    if puzzle.valida():
        print "Solution found witch %d steps \n" % depth
        print puzzle.adj_matrix
        BEST_DEPTH=depth;
        for i in range(depth):
            best_moves.insert(i, lista_movimentos[i])
        return
    
    moves = puzzle.get_legal_moves(pos_zero, played_x, played_y)
    # print moves
    if (0 <= moves[0][0] < N) and (0 <= moves[0][1] < N):
        puzzle.move(moves[0], pos_zero)
        search_dfs(puzzle, moves[0], depth+1, pos_zero[0],pos_zero[1])
        puzzle.move(pos_zero, moves[0])

    if (0 <= moves[1][0] < N) and (0 <= moves[1][1] < N):
        puzzle.move(moves[1], pos_zero)
        search_dfs(puzzle, moves[1], depth+1, pos_zero[0],pos_zero[1])
        puzzle.move(pos_zero, moves[1])

    if (0 <= moves[2][0] < N) and (0 <= moves[2][1] < N):
        puzzle.move(moves[2], pos_zero)
        search_dfs(puzzle, moves[2], depth+1, pos_zero[0],pos_zero[1])
        puzzle.move(pos_zero, moves[2])

    if (0 <= moves[3][0] < N) and (0 <= moves[3][1] < N):
        puzzle.move(moves[3], pos_zero)
        search_dfs(puzzle, moves[3], depth+1, pos_zero[0],pos_zero[1])
        puzzle.move(pos_zero, moves[3])

def main():
    global BEST_DEPTH
    puzzle = Puzzle()
    # puzzle.maximo = 800
    puzzle.pos_anterior = puzzle.find(0)
    search_dfs(puzzle, puzzle.find(0), 0, -1, -1)
    print best_moves
    return


if __name__ == '__main__':
    main()