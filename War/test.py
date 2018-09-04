class Test:
    def __init__(self, k):
        self.np = list(range(k))

    def __call__(self, n):
        return self.np[n]


tt = Test(100)

print(tt)
print(tt(3))
print(tt)
