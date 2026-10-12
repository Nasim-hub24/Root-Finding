# ------------< x**3 -x-2 >------------

def f(x):
    return x**3 -x -2
a = int (input("first initial guess = "))
b = int (input("second initial guess= "))
n = int(input("number of interations = "))
if f(a)*f(b)>0:
    print("false method fails ")
else:
    k= 1
    while (k<=n):
        c = (a*f(b)-b*f(a))/ (f(b)-f(a))
        if f(a)*f(c)<0:
            b=c
        else:
            a = c
        print("root= ",c,"at iteration= ",k)
        k = k+1



# -----------< f(x) = x*x -4 >----------

# def f(x):
#     return x**2 - 4

# a = 1.0
# b = 3.0
# tolerance = 0.0001
# max_iterations = 100

# if f(a) * f(b) >= 0:
#     print("Invalid interval")
# else:
#     for i in range(max_iterations):
#         c = (a * f(b) - b * f(a)) / (f(b) - f(a))

#         print(f"Iteration {i + 1}: c = {c:.6f}")

#         if abs(f(c)) < tolerance:
#             break

#         if f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c

#     print("Approximate root =", round(c, 6))
