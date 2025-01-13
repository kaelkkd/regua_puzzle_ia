def bfs(ruler: list):
    queue = []
    queue.append(ruler)
    nodesExpanded = 0

    while queue:
        state = queue.pop(0)
        length = len(state)
        n = (length - 1) // 2
        blank = state.index("-") #estado vazio
        nodesExpanded += 1
        print(state)

        if state == ["-"] + ["B"] * n + ["A"] * n: #presumindo que o estado meta seja o que tenha o espaco em branco como primeiro elemento ['-', 'B', 'B', 'A', 'A']
            print(f"Nos expandidos: {nodesExpanded}")
            return state
        
        else:
            for i in range(length):  #expandindo a arqvore
                if i == blank:
                    continue
                else:
                    newState = state[:] #copia do estado sem alterar o objeto original
                    aux = newState[i]
                    newState[i] = newState[blank]
                    newState[blank] = aux
                    queue.append(newState)
    