from counter import Counter

c1 = Counter(-10)
c2 = Counter(10)
c3 = Counter(10)

c1.increment()
c1.increment()
c2.increment()
c3.decrement()
# c1.reset()

print(c1)
print(c2)
print(c3)
