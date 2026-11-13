import matplotlib.pyplot as plt

def identity(n):
    E = []
    for i in range(n):
        E.append([0] * n)
    for i in range(n):
        for j in range(n):
            if i == j:
                E[i][j] = 1
            else:
                E[i][j] = 0
    return E

def lu(A):
    swap = 0
    n = len(A)
    L = identity(n)
    P = identity(n)
    U = []
    for row in A:
        U.append(list(row))
    for i in range(n):
        mx = i
        for j in range(i + 1, n):
            if abs(U[j][i]) > abs(U[mx][i]):
                mx = j
        if mx != i:
            P[i], P[mx] = P[mx], P[i]
            U[i], U[mx] = U[mx], U[i]
            swap += 1
            for k in range(i):
                L[i][k], L[mx][k] = L[mx][k], L[i][k]
        for j in range(i + 1, n):
            main = U[j][i] / U[i][i]
            L[j][i] = main
            for k in range(i, n):
                U[j][k] = U[j][k] - main * U[i][k]
    return L, U, P, swap

def vec_multiplication(A, b):
    rows = len(A)
    cols = len(A[0])
    result = [0] * rows
    for i in range(rows):
        for j in range(cols):
            result[i] = result[i] + A[i][j] * b[j]
    return result

def LB_solution(L, b):
    n = len(L)
    y = [0] * len(L)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= y[j] * L[i][j]
        y[i] /= L[i][i]
    return y

def UY_solution(U, y):
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x

def solve_system(L, U, P, b):
    Pb = vec_multiplication(P, b)
    y = LB_solution(L, Pb)
    x = UY_solution(U, y)
    return x

def mnk(X, Y, m):
    n = len(X)
    A = []
    for i in range(m + 1):
        A.append([0] * (m + 1))
    b = [0] * (m + 1)
    for i in range(m + 1):
        for j in range(m + 1):
            for k in range(n):
                A[i][j] += X[k] ** (i + j)
        for k in range(n):
            b[i] += Y[k] * X[k] ** i
    L, U, P, swap = lu(A)
    return solve_system(L, U, P, b)

def poly(coef, x):
    res = 0
    for i in range(len(coef)):
        res += coef[i] * x ** i
    return res

def error(X, Y, coef):
    s = 0
    for i in range(len(X)):
        s += (poly(coef, X[i]) - Y[i]) ** 2
    return s

def main():
    X = [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0]
    Y = [0.86603, 1.0, 0.86603, 0.5, 0.0, -0.5]
    c1 = mnk(X, Y, 1)
    c2 = mnk(X, Y, 2)
    print("многочлен 1 степени")
    print(c1)
    print("сумма квадратов ошибок")
    print(error(X, Y, c1))
    print("многочлен 2 степени")
    print(c2)
    print("сумма квадратов ошибок")
    print(error(X, Y, c2))

    xs = []
    for i in range(101):
        xs.append(-1 + 5 * i / 100)
    y1 = []
    y2 = []
    for x in xs:
        y1.append(poly(c1, x))
        y2.append(poly(c2, x))
    plt.scatter(X, Y, color="black", label="y")
    plt.plot(xs, y1, label="1 степень")
    plt.plot(xs, y2, label="2 степень")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()