import random
# a
bool2 = [random.choice([True, False]) for i in range(3)]
print(bool2)
# b
print(bool2 if all(bool2) else 'Not everything True')
# c
print(bool2 if any(bool2) else 'There are no Trues')
# d
print(bool2 if not any(bool2) else 'there is a true')
# e
print(bool2 if not all(bool2) else 'There are no Trues')
print()
# f
num2 = [random.choice([-2, 1, 0, 1, 2]) for i in range(5)]
print(num2)
# g
print(f"{'no zero in the list' if all(num2) else 'there is a zero'}")
# h
print(f"{'at least one num is not zero' if any(num2) else 'everything is a zero'}")
# i
print(f"{'everything is a zero' if not any(num2) else 'not everything is a zero'}")
# j
print(f"{'at least one zero' if not all(num2) else 'no zeroes'}")
