class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:        # return root of x
        # path compression optimization
        # if == x's root
        if x == self.root[x]:
            return x
        return self.find(self.root[x])

    def union(self, x: int, y: int) -> None:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        # rank-based union optimization
        if self.rank[rx] >= self.rank[ry]:
            self.root[ry] = rx
            rank_up = 1 if self.rank[rx] == self.rank[ry] else 0
            self.rank[rx] += rank_up
        else:
            self.root[rx] = ry

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def main():
    uf = UnionFind(10)
    # 1 - 2 - 5 - 6 - 7  3 - 8 - 9  4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # True
    print(uf.connected(4, 9))  # False

    uf.union(4, 9)
    print(uf.connected(4, 9))  # True


if __name__ == "__main__":
    main()
