numbers = [1, 7, 11, 13]

while True:
    try:
        x = int(input("Enter a number between 1-4: "))
        if 1 <= x <= 4:
            print(numbers[x-1])
        elif x == -999:
            break
        else:
            print("Please enter a number between 1-4")
    except ValueError as e:
        print(f'something went wrong --{e}-- try again')

print("ok you don't wanna play its your problem")


