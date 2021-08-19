if __name__ == '__main__':
    n = int(input())
    i = 1
    numbers = list(range(0, n))
    if not (20 < n >= 1):
        for i in range(len(numbers)):
            print(numbers[i] * numbers[i])
    else:
        exit()