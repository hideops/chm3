def find_index(X, x):
    for i in range(len(X)):
        if X[i] == x:
            return i
    return -1

def first_forward(X, Y, i):
    return (Y[i + 1] - Y[i]) / (X[i + 1] - X[i])

def first_back(X, Y, i):
    return (Y[i] - Y[i - 1]) / (X[i] - X[i - 1])

def first_center(X, Y, i):
    return (Y[i + 1] - Y[i - 1]) / (X[i + 1] - X[i - 1])

def first_second_order(X, Y, i):
    h1 = X[i] - X[i - 1]
    h2 = X[i + 1] - X[i]
    left = (Y[i] - Y[i - 1]) / h1
    right = (Y[i + 1] - Y[i]) / h2
    return left + (right - left) / (X[i + 1] - X[i - 1]) * (2 * X[i] - X[i - 1] - X[i])

def second(X, Y, i):
    h1 = X[i] - X[i - 1]
    h2 = X[i + 1] - X[i]
    left = (Y[i] - Y[i - 1]) / h1
    right = (Y[i + 1] - Y[i]) / h2
    return 2 * (right - left) / (X[i + 1] - X[i - 1])

def main():
    X = [-1.0, 0.0, 1.0, 2.0, 3.0]
    Y = [-0.5, 0.0, 0.5, 0.86603, 1.0]
    x_star = 1.0
    i = find_index(X, x_star)
    print("первая вперед")
    print(first_forward(X, Y, i))
    print("первая назад")
    print(first_back(X, Y, i))
    print("первая центральная")
    print(first_center(X, Y, i))
    print("первая 2 порядок")
    print(first_second_order(X, Y, i))
    print("вторая")
    print(second(X, Y, i))


if __name__ == "__main__":
    main()