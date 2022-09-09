import random # Usado na taxa de conexões
import time # Acompanhamento do tempo de execução

# Plotagem de Gráficos
import matplotlib.pyplot as plot 
import numpy as np

# modelagem do grafo
from no import No


# Cria conexoes aleatorias
def criaConexoes(lista_nos, taxaConexao):
    for n1 in lista_nos:
        for n2 in lista_nos:
            if random.randint(0, len(lista_nos) // taxaConexao) == 0 and (n1 is not n2) and (n1 not in n2.conexoes):
                n1.conexoes.append(n2)
                n2.conexoes.append(n1)

# Gera os nos que representaram o grafo
def geraNos(num):
    nos = []
    for i in range(num):       
        n = No(i)
        n.num = i
        nos.append(n)

    return nos


# Executa o algoritmo guloso
def executaColoracao(n, taxaConexao):
    lista_nos = geraNos(n)
    criaConexoes(lista_nos, taxaConexao)
    no_atual = 0
    cores = [0]
    
    while no_atual < n:      
        if (lista_nos[no_atual].cor == None and lista_nos[no_atual].define_cor(cores) == None):
            cores.append(len(cores))
        else: 
            no_atual += 1
    
    return cores


# Processo principal
if __name__ == '__main__':
    tempos1 = []
    tempos2 = []
    labels = [500, 1000, 2000, 4000, 8000]
    tam_barra = 0.35
    x = np.arange(len(labels))

    # Colhe amostras para taxa de 10% de criação de conexões
    for n in labels:
        inicio = time.time()
        cores = executaColoracao(n, 10)
        fim = time.time() - inicio
        print(f"Tempo de execução para n = {n}: {fim:e} segundos. Com {len(cores)} cores diferentes.")
        tempos1.append(fim)
    
    # Colhe amostras para taxa de 50% de criação de conexões
    for n in labels:
        inicio = time.time()
        cores = executaColoracao(n, 50)
        fim = time.time() - inicio
        print(f"Tempo de execução para n = {n}: {fim:e} segundos. Com {len(cores)} cores diferentes.")
        tempos2.append(fim)
    
    # Plota o gráfico comparando as complexidades
    fig, ax = plot.subplots()
    barra = ax.bar(x - tam_barra/2, tempos1, tam_barra, label="10% taxa de conexão")
    barra = ax.bar(x + tam_barra/2, tempos2, tam_barra, label="50% taxa de conexão")
    aline = ax.plot(
        x,
        [(tempos1[i]+tempos2[i])/2 for i in range(len(tempos1))],
        lw=2,
        color='black'
    )
    ax.set_ylabel("Tempo de Execução (s)")
    ax.set_xlabel("Tamanho de Entrada (n)")
    ax.set_title("Coloração de Vértices: Tempo de Execução")
    ax.set_xticks(x, labels)
    ax.legend()
    plot.show()
    


