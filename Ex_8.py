import string

def find_symbol(matrix, symbol):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == symbol:
                return i, j
    return None

num = int(input())


matrix = [input() for _ in range(num)]


symbol = input(f"Enter from {string.punctuation}: ").upper()


result = find_symbol(matrix, symbol)


if result:
    print(f"Symbol {symbol} found at coordinates: {result}")
else:
    print(f"Symbol {symbol} not found in the matrix.")
