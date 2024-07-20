import time
from UnionFind import UF
from btds_bitarray import btds_bitarray
import random as rndm


class Board:
    size = 0
    NoOfSqOpened = 0
    openclose = None
    store = None

    def connect(self, p, q):
        if self.openclose[p] and self.openclose[q]:
            self.store.union(p, q)

    def __init__(self, n):
        self.size = n
        self.NoOfSqOpened = 0
        self.store = UF((n * n) + 2)
        self.openclose = btds_bitarray(n * n + 2)
        self.openclose[0] = 1
        self.openclose[n * n + 1] = 1

    def connected(self):
        return self.store.find(0, n * n + 1)

    def OpenOneSq(self, p):
        if self.openclose[p]:
            return
        self.openclose[p] = 1
        self.NoOfSqOpened += 1

        if p == 1:  # top left corner
            self.connect(p, 2)
            self.connect(p, p + self.size)
            self.connect(p, 0)

        elif p == self.size:  # top right corner
            self.connect(p, p - 1)
            self.connect(p, p + self.size)
            self.connect(p, 0)

        elif p == self.size * (self.size - 1):  # bottom left corner
            self.connect(p, p + 1)
            self.connect(p, p - self.size)
            self.connect(p, (self.size * self.size) + 1)

        elif p == self.size * self.size:  # bottom right corner
            self.connect(p, p - 1)
            self.connect(p, p - self.size)
            self.connect(p, (self.size * self.size) + 1)

        elif p > self.size * (self.size - 1):  # bottom row
            self.connect(p, p + 1)
            self.connect(p, p - 1)
            self.connect(p, p - self.size)
            self.connect(p, (self.size * self.size) + 1)

        elif p < self.size:  # top row
            self.connect(p, p + 1)
            self.connect(p, p - 1)
            self.connect(p, p + self.size)
            self.connect(p, 0)

        elif p % self.size == 1:  # leftmost column
            self.connect(p, p + 1)
            self.connect(p, p + self.size)
            self.connect(p, p - self.size)

        elif p % self.size == 0:  # leftmost column
            self.connect(p, p - 1)
            self.connect(p, p + self.size)
            self.connect(p, p - self.size)

        else:
            self.connect(p, p + 1)
            self.connect(p, p - 1)
            self.connect(p, p + self.size)
            self.connect(p, p - self.size)


n = int(input('size of board: '))
start = time.time()
bd = Board(n)
while not bd.connected():
    x = rndm.randint(1, n * n + 1)
    bd.OpenOneSq(x)

print('percentage of sq opened to get a connectivity from top to bottom: ', (bd.NoOfSqOpened / (n * n)) * 100, 'time: ',
      time.time() - start)
