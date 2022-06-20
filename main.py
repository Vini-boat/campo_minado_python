import os
from random import *

def limparConsole(): # limpa o console
    os.system("cls" if os.name == "nt" else "clear")

def printMatriz(grid): # imprime o conteúdo da matriz com as linhas e colunas numeradas
    limparConsole()
    print("  ", end="")
    for num in range(len(grid)):
        print (f" {str(num).zfill(2)}", end="")
    print("")
    i = 0
    for row in grid:
        print (f" {str(i).zfill(2)}", end="")
        for cell in row:
           print(cell["cont"], end="")
        i += 1
        print("")

class Matrix(object):
    def __init__(self, dificuldade):
        self.rows = dificuldade['rows']
        self.cols = dificuldade['cols']
        self.qtd_bombs = dificuldade['qtd_bombs']
        self.base_cell = {'cont': ' - ', 'isbomb': False, 'ismarked': False}
        self.grid = [[self.base_cell.copy() for x in range(self.cols)] for y in range(self.rows)]

        # Gerar bombas        
        self.bombs = []
        while len(self.bombs) < self.qtd_bombs:
            x = randint(0, self.cols -1)
            y = randint(0, self.rows -1)
            if not self.cell(x, y)['isbomb'] == True:
                self.cell(x, y)['isbomb'] = True
                self.bombs.append((x, y))
        
        # Gerar a solução 
        self.solu_grid = [[self.cell(x, y).copy() for x in range(self.cols)] for y in range(self.rows)]
        for y, row in enumerate(self.solu_grid):
            for x, col in enumerate(row):
                qtd_bombs = self.aroundBombs(x, y, grid='solution')
                self.cell(x, y, grid='solution')['cont'] = f' {qtd_bombs} '
                
        
    
    def cell(self, x, y, grid='main'):
        if grid == 'main': _grid = self.grid    
        if grid == 'solution': _grid = self.solu_grid
        return _grid[y][x]

    def aroundCells(self, x, y, grid='main'):
        if grid == 'main': _grid = self.grid    
        if grid == 'solution': _grid = self.solu_grid    
        result = []
        for row in range(3):
            r_row = y + row -1
            if not r_row == -1 and not r_row == len(_grid):
                for col in range(3):
                    r_col = x + col -1
                    if not r_col == -1 and not r_col == len(_grid[0]):
                        if r_row == 0 and r_col == 0: 
                            continue
                        result.append((r_col, r_row))
        
        return result

    def aroundBombs(self, x, y, grid='main'):
        _grid = grid
        around_cells = self.aroundCells(x, y, grid=_grid)
        qtd_bombs = 0
        
        for cell in around_cells:
            _x = cell[0]
            _y = cell[1]
            if self.cell(_x, _y, grid=_grid)['isbomb']: qtd_bombs += 1
        
        return qtd_bombs
    
    def openCell(self, x, y, memo={}):
        self.cell(x, y)['cont'] = self.cell(x, y, grid='solution')['cont']
        
        if (x, y) in memo: return
        memo[(x, y)] = True
        
        if self.cell(x, y)['cont'] != ' 0 ': return
        else:
            around_cells = self.aroundCells(x, y)

            for cell in around_cells:
                _x = cell[0]
                _y = cell[1]
                self.openCell(_x, _y)      

def click(obj_matrix, x, y):
    if obj_matrix.cell(x, y)['cont'] != ' - ': 
        print('escolha uma celula que ainda não foi aberta')
        return
    
    if obj_matrix.cell(x, y)['isbomb']:
        print('voce perdeu')
        return
    else:
        obj_matrix.openCell(x, y)

def getCord():
    temp = input('escolha uma célula (x, y): ')
    temp = temp.split(',')
    cord = (int(temp[0]), int(temp[1]))
    print(cord)
    return cord

def getAction():
    while True:
        act = input('(m)arcar ou (a)brir? ')
        if act == 'm':
            return 'marcar'
        elif act == 'a': 
            return 'abrir'

def marcar(matrix, x, y):
    if matrix.cell(x, y)['ismarked']:
        matrix.cell(x, y)['ismarked'] = False
        matrix.cell(x, y)['cont'] = ' - '
    elif not matrix.cell(x, y)['ismarked']:
        matrix.cell(x, y)['ismarked'] = True
        matrix.cell(x, y)['cont'] = ' X '
    


def jogo():
    perdeu = False
    ganhou = False
    while not perdeu or ganhou:
        printMatriz(grid.grid)
        print(grid.bombs)
        action = getAction()
        cord = getCord()
        x = cord[0]
        y = cord[1]
        if action == 'abrir':
            if grid.cell(x, y)['isbomb']:
                perdeu =True
            else:
                click(grid,x, y)
        elif action == 'marcar':
            marcar(grid, x, y)
        
        for bomb in grid.bombs:
            _x = bomb[0]
            _y = bomb[1]
            grid.cell(_x, _y)['ismarked'] = True

        ganhou = True
        for bomb in grid.bombs:
            _x = bomb[0]
            _y = bomb[1]
            if not grid.cell(_x, _y)['ismarked']:
                ganhou = False
                break
            
    if perdeu: print('você perdeu')
    if ganhou: print('você ganhou')


if __name__ == '__main__':
    dificuldade = {'dificuldade': 'fácil', 'rows': 9, 'cols': 9, 'qtd_bombs': 10}
    grid = Matrix(dificuldade)
    jogo()

