import random
# a
a: list[int] = [i for i in range(95, 106)]
print(a)
# b
b: list[int] = [i for i in range(10, 21, 2)]
print(b)
# c
c = [random.choice([True, False]) for _ in range(5)]
print(c)
# d
# I will use _ instead of 'i' as a statement for not using the variable in the "for" loop
# helps the reader understand the code better, and not to search for it when looking for mistakes
# e
e = [random.randint(1,100) for _ in range(10)]
print(e)
# f
f = [i for i in e if i > 50]
print(f)
# g
g = [i for i in (random.randint(1, 100) for _ in range(10)) if i > 50]
print(g)
# h
h = [c for c in input("give a sentence") if c != ' ' and c != 't']
print(h)