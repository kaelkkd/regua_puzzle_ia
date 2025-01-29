from src import Regua
import time

def bfs(ruler: Regua):
    """
    Realiza a busca em largura para encontrar a solucao do problema da regua a partir de um estado inicial pertencente a uma regua

    Parametros:
            ruler(Regua): objeto que representa a regua (sera utilizado o atributo ruler como estado inicial)

    Retorno:
            state(list): estado final da regua
    """
    queue = []
    queue.append(ruler.ruler)
    statesVisited = set()
    nodesExpanded = 0
    maxMemoryUsed = 1
    startTime = time.time()
    
    while queue:
        state = queue.pop(0)
        stateTuple = tuple(state)
        if stateTuple in statesVisited:
            continue
        statesVisited.add(stateTuple)
        length = len(state)
        n = (length - 1) // 2
        blank = state.index("-") #estado vazio
        nodesExpanded += 1
        maxMemoryUsed = max(maxMemoryUsed, len(queue))


        if state == ["-"] + ["B"] * n + ["A"] * n: #presumindo que o estado meta seja o que tenha o espaco em branco como primeiro elemento ['-', 'B', 'B', 'A', 'A'] 
            endTime = time.time()
            print(f"Nos expandidos: {nodesExpanded}")
            print(f"Quantidades de passos: {len(statesVisited) - 1}")
            print(f"Memoria maxima utilizada(nos na fronteira): {maxMemoryUsed}")
            print(f"Tempo de execucao do BFS para uma regua de tamanho {ruler.size}: {(endTime - startTime): .10f}\n")
            return state
        else:
            for i in range(length):  #expandindo a arqvore
                if i == blank:
                    continue
                newState = state[:] #copia do estado sem alterar o objeto original
                aux = newState[i]
                newState[i] = newState[blank]
                newState[blank] = aux
                queue.append(newState)

    print("Nao foi possivel encontar uma solucao")

    return None