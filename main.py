import time
from src import bfs
from src import Regua

if __name__ == '__main__':
    test = Regua(5)
    startTime = time.time()
    a = bfs(test.ruler)
    endTime = time.time()
    print(f"Tempo de execucao do BFS para uma regua de tamanho {test.size}: {(endTime - startTime): .6f}")