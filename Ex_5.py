number = int(input())
matrix = []
for i in range(number):
    matrix.append(list(map(int, input().split(", "))))

sum =sum(matrix[i][number-i-1] for i in range(number))

print(sum)
    