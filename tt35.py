def f(x):
    return x / (3 * x + 4) ** 2

def rectangles(a, b, h):
    n = int(round((b - a) / h))
    s = 0
    for i in range(n):
        s += f(a + h * i + h / 2)
    return s * h

def trapezoid(a, b, h):
    n = int(round((b - a) / h))
    s = (f(a) + f(b)) / 2
    for i in range(1, n):
        s += f(a + h * i)
    return s * h

def simpson(a, b, h):
    n = int(round((b - a) / h))
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            s += 2 * f(a + h * i)
        else:
            s += 4 * f(a + h * i)
    return s * h / 3

def runge(F1, F2, h1, h2, p):
    k = h1 / h2
    return F2 + (F2 - F1) / (k ** p - 1)

def main():
    a = 0
    b = 4
    h1 = 1.0
    h2 = 0.5
    R1 = rectangles(a, b, h1)
    R2 = rectangles(a, b, h2)
    T1 = trapezoid(a, b, h1)
    T2 = trapezoid(a, b, h2)
    S1 = simpson(a, b, h1)
    S2 = simpson(a, b, h2)
    print("прямоугольники h1")
    print(R1)
    print("прямоугольники h2")
    print(R2)
    print("трапеции h1")
    print(T1)
    print("трапеции h2")
    print(T2)
    print("симпсон h1")
    print(S1)
    print("симпсон h2")
    print(S2)
    print("рунге прямоугольники")
    print(runge(R1, R2, h1, h2, 2))
    print("рунге трапеции")
    print(runge(T1, T2, h1, h2, 2))
    print("рунге симпсон")
    print(runge(S1, S2, h1, h2, 4))
    print("погрешность прямоугольники")
    print(abs(R2 - runge(R1, R2, h1, h2, 2)))
    print("погрешность трапеции")
    print(abs(T2 - runge(T1, T2, h1, h2, 2)))
    print("погрешность симпсон")
    print(abs(S2 - runge(S1, S2, h1, h2, 4)))


if __name__ == "__main__":
    main()