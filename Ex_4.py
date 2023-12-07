number = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(number)]

sum =sum(matrix[i][i] for i in range(number))
print(sum)
    
