# ----------< x**x - x*x -2 >-----------

def f(x):
    return x**3-x*x-2
def df(x):
    return 3*x*x - 2*x
a = float(input("initial guess= "))
n = int(input("number interactions "))
k=1
while(k<=n):
    r = a- f(a)/df(a)
    print("root = ", r, "at iteration",k)
    k = k+1
    a =r


# ------------< f(x) = x*x -4 = 0 >-------------

# def f(x):
#     return x**2 - 4

# def df(x):
#     return 2 * x

# x = 3.0  # Initial guess
# tolerance = 0.0001
# max_iterations = 100

# for i in range(max_iterations):
#     if df(x) == 0:
#         print("Derivative is zero!")
#         break

#     x_new = x - f(x) / df(x)

#     print(f"Iteration {i + 1}: x = {x_new:.6f}")

#     if abs(x_new - x) < tolerance:
#         x = x_new
#         break

#     x = x_new

# print("Approximate root =", x)

