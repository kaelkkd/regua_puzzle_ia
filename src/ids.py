from src import Regua
import time

def dfs(state: list, meta: list, depth: int, nodesExpanded: int, maxMemoryUsed: int, statesVisited: set, currDepth: int):
    maxMemoryUsed = max(maxMemoryUsed, currDepth)
    if state == meta:
        return True, nodesExpanded, maxMemoryUsed
    if depth <= 0:
        return False, nodesExpanded, maxMemoryUsed
    
    print(state)
    blank = state.index("-")
    n = (len(state) - 1) // 2
    for i in range(max(0, blank - n), min(len(state), blank + n + 1)): #busca somente nos vizinhos do estado vazio
        if i == blank:
            continue
        newState = state[:]
        newState[blank] = newState[i]
        newState[i] = "-"
        
        if tuple(newState) not in statesVisited:
            statesVisited.add(tuple(newState))
            nodesExpanded += 1
            result, nodesExpanded, maxMemoryUsed = dfs(newState, meta, depth - 1, nodesExpanded, maxMemoryUsed, statesVisited, currDepth + 1)
            if result:
                return True, nodesExpanded, maxMemoryUsed
            
    return False, nodesExpanded, maxMemoryUsed

def ids(ruler: Regua, maxDepth = 100):
    """
    Realiza a busca em profundidade iterativa para encontrar a solucao do problema da regua a partir de um estado inicial pertencente a uma regua.
    A profundidade maxima padrao e 100, mas pode ser alterada.

    Parametros:
            ruler(Regua): objeto que representa a regua (sera utilizado o atributo ruler como estado inicial)
            maxDepth(int): profundidade maxima para a busca

    Retorno:
            result(list): estado final da regua
    """
    
    startTime = time.time()
    n = (ruler.size - 1) // 2
    meta = ["-"] + ["B"] * n + ["A"] * n
    nodesExpanded = 0
    maxMemoryUsed = 1
    depth = 0

    while depth <= maxDepth:
        statesVisited = set() #dentro do loop pois o conjunto de estados visitados deve ser zerado a cada nova busca
        result, nodesExpanded, maxMemoryUsed = dfs(ruler.ruler, meta, depth, nodesExpanded, maxMemoryUsed, statesVisited, 1)
        if result:           
            endTime = time.time()
            print(f"Nos expandidos: {nodesExpanded}")
            print(f"Profundidade: {depth}")
            print(f"Memoria maxima utilizada(nos na fronteira): {maxMemoryUsed}")
            print(f"Tempo de execucao do IDS para uma regua de tamanho {ruler.size}: {(endTime - startTime): .6f}\n")
            return result
        depth += 1

