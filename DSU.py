class DSU:
    def __init__(self, n: int):
        self.root = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        return self.find(self.root[x])

    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        rank_x, rank_y = self.rank[root_x], self.rank[root_y]
        if rank_x >= rank_y:
            self.root[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            rank_up = 1 if rank_x == rank_y else 0
            self.rank[root_x] += rank_up
        else:
            self.root[root_x] = root_y
            self.size[root_y] += self.size[root_x]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
