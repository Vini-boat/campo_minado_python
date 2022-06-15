import os
from random import Random, randint, random


def limparConsole():
    os.system("cls" if os.name == "nt" else "clear")

def gerarMatriz(size):
    return [[{"content":' - ',"isbomb": False}for _ in range(size['cols'])] for _ in range(size['rows'])]

def printMatriz(matriz):
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

def telaEscolherDificuldade():
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

def getCoordenada():
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
        


def escolherCelula(matriz, coordenada):
    matriz[coordenada[1]][coordenada[0]]["content"] = ' X '

def jogo():
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

def gerarBombas():
    qtd_bombas = dificuldade["qtd_bombas"]
    rows = dificuldade["rows"]
    cols = dificuldade["cols"]
    bombas_geradas = 0
    while bombas_geradas < qtd_bombas:
        x = randint(0, cols - 1)
        y = randint(0, rows - 1)
        matrix[y][x]["isbomb"] = True
        bombas_geradas += 1


if __name__ == "__main__":
    dificuldade = telaEscolherDificuldade()
    matrix = gerarMatriz(dificuldade)
    gerarBombas()
    jogo()
    
