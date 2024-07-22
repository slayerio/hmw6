# a
temp: list[float] = []
# b
while True:
    temperature: float = float(input("enter temperature [-999 to exit]:"))
    if temperature == -999:
        break
    if temperature < -50 or temperature > 50:
        continue
    temp.append(temperature)
# c
temp.extend([18.5, 39.1, -20.0])
print(temp)
# d,e,f
print(f"max temp = {max(temp)}")
print(f"min temp = {min(temp)}")
print(f"avg temp = {sum(temp) / len(temp): .2f}")
# g
import statistics
print(f"avg temp = {statistics.mean(temp): .2f}")
# h
del temp[0]
print(temp)
# i
temp.remove(18.5)
print(temp)
# j
last_temp = temp.pop(-1)
print(temp)
# k
clone = temp.copy()
clone.sort()
print(clone)
# l
clone2 = temp.copy()
clone2.sort(reverse=True)
print(clone2)

# m
# sort changes the list itsel (thats why we need a copy of the list to sort)
# sorted does not change the list, only for the print, so we dont need a copy

# n
# reversed gives you "Iterator" allowing a reversed numbers from the list but in a diff' obj.
# to change it back: reversed_list = list(reversed(my_list))