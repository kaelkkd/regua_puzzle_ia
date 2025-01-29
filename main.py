from src import Regua, bfs, ids, aStar

if __name__ == '__main__':
    test = Regua(21)
    c = aStar(test)
    d = aStar(test, False)
    b = ids(test)
    a = bfs(test)