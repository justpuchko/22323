number = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(number)]
sum = sum(matrix[i][j] for i in range(number) for j in range(i + 1))
print(sum)