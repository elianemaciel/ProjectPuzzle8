# -*- coding: utf-8 -*-


goal_state = [[1,3, 2],
            [8,0,4],
            [7,6, 5]]

class Puzzle:

    def __init__(self):
        # search depth of current instance
        self.maximo = 0
        # parent node in search path
        self.adj_matrix = []
        self.lista_movimentos = {}
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

    def get_legal_moves(self):
        """Retorna lista de movimentos possíveis"""
        # get row and column of the empty piece
        row, col = self.find(0)
        free = []
        
        # find which pieces can move there
        if row > 0:
            if not (row-1, col) == self.pos_anterior:
                free.append((row - 1, col))
        if col > 0:
            if not (row, col-1) == self.pos_anterior:
                free.append((row, col - 1))
        if row < 2:
            if not (row+1, col) == self.pos_anterior:
                free.append((row + 1, col))
        if col < 2:
            if not (row, col+1) == self.pos_anterior:
                free.append((row, col + 1))

        return free

    def move(self, pos):
        """Movimenta puzzle"""
        # get row and column of the empty piece
        print pos
        if not self.linha1 or (self.linha1 and pos[0] != 0):
            row_ini, col_ini = self.find(0)
            aux = self.adj_matrix[pos[0]][pos[1]]
            self.adj_matrix[row_ini][col_ini] = aux
            self.adj_matrix[pos[0]][pos[1]] = 0
            self.pos_anterior = (row_ini, col_ini)
            if self.lista_movimentos.get((row_ini, col_ini)):
                if len(self.lista_movimentos.get((row_ini, col_ini))) == 4:
                    self.lista_movimentos[(row_ini, col_ini)] = []  
                self.lista_movimentos[(row_ini, col_ini)].append(pos)
            else:
                self.lista_movimentos[(row_ini, col_ini)] = [pos]
            self.lista_posicoes.append((row_ini, col_ini))

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
    print puzzle.adj_matrix
    if puzzle.valida():
        print puzzle.adj_matrix
        return
    else:
        moves = puzzle.get_legal_moves()
        print moves
        for move in moves:

            if  not move == puzzle.pos_anterior:
                print "MOVE", move
                puzzle.move(move)
        if n < puzzle.maximo:
            back(puzzle.find(0), puzzle, n+1)
        else:
            return

def main():
    lista_movimentos = []
    puzzle = Puzzle()
    puzzle.maximo = 800
    puzzle.pos_anterior = puzzle.find(0)
    back(puzzle.find(0), puzzle, 1)
    return


if __name__ == '__main__':
    main()