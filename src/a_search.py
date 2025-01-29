import heapq
import time
from src import Regua

def manhattanDistance(ruler: list, meta: list):
    distance = 0
    for element in ruler:
        if element != "-": #estado vazio
            currentPos = ruler.index(element)
            metaPos = meta.index(element)
            distance += abs(currentPos - metaPos)

    return distance

# Heurística 2: Número de Inversões
def inversion(ruler: list, meta: list):
    inversions = 0
    for i in range(len(ruler)):
        for j in range(i + 1, len(ruler)):
            if ruler[i] != "-" and ruler[j] != "-" and meta.index(ruler[i]) > meta.index(ruler[j]):
                inversions += 1
    return inversions

def aStar(ruler: Regua, manhattan = True):
    """
    Realiza a busca A* para encontrar a solucao do problema da regua a partir de um estado inicial pertencente a uma regua.
    Por padrao, o algorimo utiliza a distancia de manhattan como heuristica, mas pode ser alterado para o numero de inversoes.

    Parametros:
            ruler(Regua): objeto que representa a regua (sera utilizado o atributo ruler como estado inicial)
            manhattan(bool): se True, utiliza a distancia de manhattan como heuristica, caso contrario, utiliza o numero de inversoes

    Retorno:
            state(list): estado final da regua
    """
    startTime = time.time()
    queue = []
    n = (ruler.size - 1) // 2
    meta = ["-"] + ["B"] * n + ["A"] * n #estado meta igual o bfs
    if manhattan:
        startH = manhattanDistance(ruler.ruler, meta) #heuristica do estado atual para o meta
    else:
        startH = inversion(ruler.ruler, meta)
    heapq.heappush(queue, (startH, 0, ruler.ruler)) #startH como f(x) pois g(x) = 0
    statesVisited = set()
    nodesExpanded = 0
    maxMemoryUsed = 1
    
    while queue:
        fValue, gValue, currentState = heapq.heappop(queue)
        blank = currentState.index("-") #estado vazio
        nodesExpanded += 1
        maxMemoryUsed = max(maxMemoryUsed, len(queue))
        print(f"f(x): {fValue}\n Estado: {currentState}")
        if currentState == meta:
            endTime = time.time()
            print(f"Nos expandidos: {nodesExpanded}")
            print(f"Quantidades de passos: {gValue}")
            print(f"Memoria maxima utilizada(nos na fronteira): {maxMemoryUsed}")
            print(f"Tempo de execucao da busca A*(distancia de manhattan) para uma regua de tamanho {ruler.size}: {(endTime - startTime): .6f}")
           
            return currentState

        for i in range(len(currentState)):  #expandindo a arqvore. -1 pois o ultimo elemento nao precisa ser trocado
            if i == blank:
                continue
            newState = currentState[:] #copia do estado sem alterar o objeto original
            aux = newState[i]
            newState[i] = newState[blank]
            newState[blank] = aux
            movementCost = abs(i - blank)
            newStateGValue = gValue + movementCost  #g(x) do novo estado
            if tuple(newState) not in statesVisited:
                heapq.heappush(queue, (newStateGValue + manhattanDistance(newState, meta), newStateGValue, newState))
                statesVisited.add(tuple(newState))
    
    print("Nao foi possivel encontrar uma solucao")    

    return None