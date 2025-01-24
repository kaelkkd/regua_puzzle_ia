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

def aStar(ruler: Regua):
    startTime = time.time()
    queue = []
    n = (ruler.size - 1) // 2
    meta = ["-"] + ["B"] * n + ["A"] * n #estado meta igual o bfs
    startH = manhattanDistance(ruler.ruler, meta) #heuristica do estado atual para o meta
    heapq.heappush(queue, (startH, 0, ruler.ruler)) #startH como f(x) pois g(x) = 0
    statesVisited = set()
    nodesExpanded = 0
    
    while queue:
        fValue, gValue, currentState = heapq.heappop(queue)
        blank = currentState.index("-") #estado vazio
        nodesExpanded += 1
        print(f"f(x): {fValue}\n Estado: {currentState}")
        if currentState == meta:
            print(f"Nos expandidos: {nodesExpanded}")
            endTime = time.time()
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