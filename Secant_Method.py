
# -------< x**2 -4 >--------

def f(x):
    return x**2 - 4

x0 = 1.0
x1 = 3.0
tolerance = 0.0001
max_iterations = 100

for i in range(max_iterations):
    if f(x1) - f(x0) == 0:
        print("Division by zero!")
        break

    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

    print(f"Iteration {i + 1}: x = {x2:.6f}")

    if abs(x2 - x1) < tolerance:
        x1 = x2
        break

    x0 = x1
    x1 = x2

print("Approximate root =", round(x1, 6))
