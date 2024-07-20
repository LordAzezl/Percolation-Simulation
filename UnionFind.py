import numpy as ny


class UF:
    size = 0
    id1 = []

    def __init__(self, n):
        self.id1 = ny.arange(n, dtype=int)  # O(n)
        self.size = n

    def find(self, p, q):  # O(1) independent of 1
        return self.id1[p] == self.id1[q]

    def union(self, p, q):
        x = self.id1[p]
        for i in range(self.size):
            if self.id1[i] == x:
                self.id1[i] = self.id1[q]
