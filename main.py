import os
from random import *

def limparConsole(): # limpa o console
    os.system("cls" if os.name == "nt" else "clear")

def printMatriz(grid): # imprime o conteúdo da matriz com as linhas e colunas numeradas
    # limparConsole()
    print("  ", end="")
    for num in range(len(grid)):
        print (f" {str(num).zfill(2)}", end="")
    print("")
    i = 0
    for row in grid:
        print (f" {str(i).zfill(2)}", end="")
        for cell in row:
            if cell['isbomb']:
                print(' B ', end="") # temp
            else:
                print(cell["cont"], end="")
        i += 1
        print("")

class Matrix(object):
    def __init__(self, dificuldade):
        self.rows = dificuldade['rows']
        self.cols = dificuldade['cols']
        self.qtd_bombs = dificuldade['qtd_bombs']
        self.base_cell = {'cont': ' - ', 'isbomb': False}
        self.grid = [[self.base_cell.copy() for x in range(self.cols)] for y in range(self.rows)]

        # Gerar bombas        
        bombs = 0
        while bombs <= self.qtd_bombs:
            x = randint(0, self.cols -1)
            y = randint(0, self.rows -1)
            self.cell(x, y)['isbomb'] = True
            bombs += 1
        
        # Gerar a solução 
        self.solu_grid = [[self.cell(x, y).copy() for x in range(self.cols)] for y in range(self.rows)]
        self.solu_dict = {}
        for y in range(len(self.solu_grid)):
            for x in range(len(self.solu_grid[0])):
                self.solu_dict[f'{x}.{y}'] = self.solu_grid[y][x]
        
    
    def cell(self, x, y):
        return self.grid[y][x]
        


if __name__ == '__main__':
    dificuldade = {'dificuldade': 'fácil', 'rows': 9, 'cols': 9, 'qtd_bombs': 10}
    grid = Matrix(dificuldade)
    printMatriz(grid.grid)

