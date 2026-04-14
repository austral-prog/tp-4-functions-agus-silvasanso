def roots(a, b, c):
    discriminante = (b**2) - (4 * a * c)
    if discriminante < 0:
        return "( )"
    elif discriminante == 0:
        r1 = (-b) / (2 * a)
        return f"({r1})"
    else:
        r1 = (-b + (discriminante**0.5)) / (2 * a)
        r2 = (-b - (discriminante**0.5)) / (2 * a)
        return f"({r1}, {r2})"

def value_y(a, b, c, x):
    return a * (x**2) + b * x + c

def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a == 0 and c == 0:
        return f"f(x) = {b} * X"
    elif c == 0 and b == 0:
        return f"f(x) = {a} * X^2"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    d1 = 2 * a
    if a == 0 and b == 0:
        return "f'(x) = 0"
    elif a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {d1} * X"
    else:
        return f"f'(x) = {d1} * X + {b}"
