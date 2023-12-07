def largest_square(matrix):
    max_sum = 0
    top_left = (0, 0)
    
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows - 1):
        for j in range(cols - 1):
            current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
            
            if current_sum > max_sum:
                max_sum = current_sum
                top_left = (i, j)

    return top_left, max_sum


number = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(number)]

top_left, max_sum = largest_square(matrix)

for i in range(top_left[0], top_left[0] + 2):
    for j in range(top_left[1], top_left[1] + 2):
        print(matrix[i][j], end=" ")
    print()

print(max_sum)
