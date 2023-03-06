def main():
    print("Hello :) Please, enter matrix dimension separated by space:")
    m, n = input().split(' ')
    m = int(m)
    n = int(n)

    print("Please, write elements of matrix row by row. Separate numbers by space:")
    matrix = []
    for i in range(m):
        row_elements = input().split(' ')
        row_elements = [int(element) for element in row_elements[:n]]
        matrix.append(row_elements)


if __name__ == "__main__":
    main()