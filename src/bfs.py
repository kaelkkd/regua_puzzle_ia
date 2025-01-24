from src import Regua
import time

def bfs(ruler: Regua):
    queue = []
    queue.append(ruler.ruler)
    statesVisited = set()
    nodesExpanded = 0
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
        print(state)

        if state == ["-"] + ["B"] * n + ["A"] * n: #presumindo que o estado meta seja o que tenha o espaco em branco como primeiro elemento ['-', 'B', 'B', 'A', 'A'] 
            print(f"Nos expandidos: {nodesExpanded}")
            endTime = time.time()
            print(f"Tempo de execucao do BFS para uma regua de tamanho {ruler.size}: {(endTime - startTime): .6f}")
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