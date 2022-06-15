import os
from random import Random, randint, random


def limparConsole(): # limpa o console
    os.system("cls" if os.name == "nt" else "clear")

def gerarMatriz(size): # retorna uma matriz nula sem bombas
    return [[{"content":' - ',"isbomb": False}for _ in range(size['cols'])] for _ in range(size['rows'])]

def printMatriz(matriz): # imprime o conteúdo da matriz com as linhas e colunas numeradas
    limparConsole()
    print("  ", end="")
    for num in range(len(matrix)):
        print (f" {str(num).zfill(2)}", end="")
    print("")
    i = 0
    for row in matriz:
        print (f" {str(i).zfill(2)}", end="")
        for element in row:
            print(element["content"], end="")
        i += 1
        print("")

def escolherDificuldade(): # printa uma tela com a escolha de dificuldade e espera uma imput do usuário
    limparConsole()
    print("""
    Escolha a dificuldade do jogo:

    1 - fácil
    2 - médio
    3 - difícil
    """)
    while True:
        escolha = input('    ')
        if escolha == '1':
            return {"dificuldade": 'fácil',"cols":7, "rows": 7, "qtd_bombas": 5}
        elif escolha == '2':
            return {"dificuldade": 'média',"cols":15, "rows": 15, "qtd_bombas": 10}
        elif escolha == '3':
            return {"dificuldade": 'difícil',"cols":25, "rows": 25, "qtd_bombas": 20}
        else:
            print('escolha entre as dificuldades disponibilizadas')
            continue
        break

def getCoordenada(): # Recebe uma coordenada do usuário e garante que ela seja válida para o jogo
    print('digite a coordenada desejada (x,y):')
    while True:
        temp = input()
        if temp.count(',') == 1:
            temp = temp.split(',')
            if temp[0].isdecimal() and temp[1].isdecimal():
                temp[0] = int(temp[0])
                temp[1] = int(temp[1])
                break
        
        print('escreva coordenadas válidadas:')
    return (temp[0], temp[1])
        


def escolherCelula(coordenada): # Muda o conteudo da célula na coordenada passada para um " X "
    x = coordenada[0]
    y = coordenada[1]
    matrix[y][x]["content"] = ' X '


def gerarBombas(): # gera bombas na matriz baseado na dificuldade selecionada
    qtd_bombas = dificuldade["qtd_bombas"]
    rows = dificuldade["rows"]
    cols = dificuldade["cols"]
    bombas_geradas = 0
    while bombas_geradas <= qtd_bombas:
        x = randint(0, cols - 1)
        y = randint(0, rows - 1)
        matrix[y][x]["isbomb"] = True
        bombas_geradas += 1
    
def bombsAround(coordenada): # retorna o número de bombas ao redor da célula selecionada
    x = coordenada[0]
    y = coordenada[1]
    qtd = 0
    
    if not matrix[y][x]['isbomb']:
        for r_row in range(3):
            if not y + r_row -1 == -1 and not y + r_row -1 == len(matrix):
                for r_col in range(3):
                    if not x + r_col -1 == -1 and not x + r_col -1 == len(matrix[0]):
                        if matrix[y + r_row -1][x + r_col -1]["isbomb"]: 
                            qtd += 1
    return qtd    

def jogo(): # instancia do jogo em si, entra em um loop e define a condição de derrota
    perdeu = False
    while not perdeu:
        printMatriz(matrix)
        for i in matrix: print(i)
        coordenada = getCoordenada()
        escolherCelula(matrix, coordenada)
        if matrix[coordenada[1]][coordenada[0]]["isbomb"]:
            perdeu = True

    printMatriz(matrix)
    print('você perdeu')

if __name__ == "__main__":
    dificuldade = escolherDificuldade()
    matrix = gerarMatriz(dificuldade)
    matrix[1][1]["isbomb"] = True
    matrix[3][3]["isbomb"] = True
    matrix[4][4]["isbomb"] = True
    matrix[6][6]["isbomb"] = True
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]["isbomb"]:
                matrix[row][col]["content"] = " X "
            else:
                matrix[row][col]["content"] = f" {bombsAround((col, row))} "
    printMatriz(matrix)
    for i in matrix:
        print(i)
    
