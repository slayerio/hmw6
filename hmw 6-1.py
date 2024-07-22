# a
empty: list[int] = []
for i in range(80,100):
    empty.append(i)
print(empty)
# b,c
print(empty[0])
print(empty[-1])
# d
print(f"there are {len(empty)} numbers in the list")
# e
print(empty[3:13])
# f
print(empty[3:])
# g
print(empty[:9])
# h
empty.insert(10,999) ##(0-10),999,12-21
print(empty)
# i
print(empty[::-1])
# j
empty.pop(10)
print(empty[1::2])
