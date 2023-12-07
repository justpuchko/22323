number = int(input())
matrix = [[(col + 1 +row * number )for col in range(number)] for row in range(number)]

for row in matrix:
    print(row, sum(row))
