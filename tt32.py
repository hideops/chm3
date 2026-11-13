def progonka(A, b):
    n = len(A)
    P = [0] * n
    Q = [0] * n
    x = [0] * n
    P[0] = -A[0][1] / A[0][0]
    Q[0] = b[0] / A[0][0]
    for i in range(1, n):
        c = A[i][i]
        a = A[i][i - 1]
        if i < n - 1:
            P[i] = -A[i][i + 1] / (c + a * P[i - 1])
        Q[i] = (b[i] - a * Q[i - 1]) / (c + a * P[i - 1])
    x[n - 1] = Q[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = P[i] * x[i + 1] + Q[i]
    return x

def spline_coef(X, F):
    n = len(X) - 1
    h = []
    for i in range(n):
        h.append(X[i + 1] - X[i])
    A = []
    for i in range(n - 1):
        A.append([0] * (n - 1))
    b = []
    for i in range(1, n):
        row = i - 1
        if i > 1:
            A[row][row - 1] = h[i - 1]
        A[row][row] = 2 * (h[i - 1] + h[i])
        if i < n - 1:
            A[row][row + 1] = h[i]
        b.append(3 * ((F[i + 1] - F[i]) / h[i] - (F[i] - F[i - 1]) / h[i - 1]))
    c_mid = progonka(A, b)
    c = [0] + c_mid + [0]
    a = []
    bb = []
    d = []
    for i in range(n):
        a.append(F[i])
        bb.append((F[i + 1] - F[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3)
        d.append((c[i + 1] - c[i]) / (3 * h[i]))
    return a, bb, c[:-1], d

def spline_value(X, a, b, c, d, x):
    n = len(X) - 1
    k = 0
    for i in range(n):
        if X[i] <= x <= X[i + 1]:
            k = i
            break
    dx = x - X[k]
    return a[k] + b[k] * dx + c[k] * dx ** 2 + d[k] * dx ** 3

def main():
    X = [0.0, 1.0, 2.0, 3.0, 4.0]
    F = [1.0, 0.86603, 0.5, 0.0, -0.5]
    x_star = 1.5
    a, b, c, d = spline_coef(X, F)
    print("a")
    print(a)
    print("b")
    print(b)
    print("c")
    print(c)
    print("d")
    print(d)
    print("S")
    print(spline_value(X, a, b, c, d, x_star))


if __name__ == "__main__":
    main()