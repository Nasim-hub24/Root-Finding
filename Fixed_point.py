
# -----------< x**x +x -2 >---------

import math

def g(x):
    return math.sqrt(2 - x)

x = 1.5  # Initial guess
tolerance = 0.0001
max_iterations = 100

for i in range(max_iterations):
    x_new = g(x)

    print(f"Iteration {i + 1}: x = {x_new:.6f}")

    if abs(x_new - x) < tolerance:
        x = x_new
        break

    x = x_new

print("Approximate root =", round(x, 6))
