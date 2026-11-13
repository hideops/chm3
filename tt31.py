import math

def f(x):
    return math.cos(x)

def lagr(X, Y, x):
    n = len(X)
    res = 0
    for i in range(n):
        li = 1
        for j in range(n):
            if i != j:
                li = li * (x - X[j]) / (X[i] - X[j])
        res += Y[i] * li
    return res

def lagr_str(X, Y):
    n = len(X)
    s = ""
    for i in range(n):
        num = ""
        den = 1
        for j in range(n):
            if i != j:
                num += "(x - " + str(round(X[j], 5)) + ")"
                den = den * (X[i] - X[j])
        s += "(" + str(round(Y[i] / den, 5)) + ")*" + num
        if i != n - 1:
            s += " + "
    return s

def diff_table(X, Y):
    n = len(X)
    T = []
    for i in range(n):
        T.append([0] * n)
    for i in range(n):
        T[i][0] = Y[i]
    for j in range(1, n):
        for i in range(n - j):
            T[i][j] = (T[i + 1][j - 1] - T[i][j - 1]) / (X[i + j] - X[i])
    return T

def newton(X, T, x):
    n = len(X)
    res = T[0][0]
    mult = 1
    for i in range(1, n):
        mult = mult * (x - X[i - 1])
        res += T[0][i] * mult
    return res

def newton_str(X, T):
    n = len(X)
    s = str(round(T[0][0], 5))
    mult = ""
    for i in range(1, n):
        mult += "(x - " + str(round(X[i - 1], 5)) + ")"
        s += " + (" + str(round(T[0][i], 5)) + ")*" + mult
    return s

def solve(X, x_star):
    Y = []
    for x in X:
        Y.append(f(x))
    print("X")
    print(X)
    print("Y")
    print(Y)
    print("многочлен лагранжа")
    print(lagr_str(X, Y))
    L = lagr(X, Y, x_star)
    print("лагранж")
    print(L)
    T = diff_table(X, Y)
    print("таблица")
    for row in T:
        print(row)
    print("многочлен ньютона")
    print(newton_str(X, T))
    N = newton(X, T, x_star)
    print("ньютон")
    print(N)
    exact = f(x_star)
    print("точное значение")
    print(exact)
    print("погрешность лагранжа")
    print(abs(exact - L))
    print("погрешность ньютона")
    print(abs(exact - N))

def main():
    x_star = math.pi / 4
    print("2а")
    Xa = [0, math.pi / 6, 2 * math.pi / 6, 3 * math.pi / 6]
    solve(Xa, x_star)
    print("2б")
    Xb = [0, math.pi / 6, 5 * math.pi / 12, math.pi / 2]
    solve(Xb, x_star)


if __name__ == "__main__":
    main()