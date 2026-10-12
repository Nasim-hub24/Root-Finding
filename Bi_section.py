
# -----------< x**3 -x -4 >-----------

def f(x):
    return x**3 -x -4
a = int(input("first initial guess= "))
b = int(input("second initial guess= "))

if f(a)*f(b)<0:
    print("bisection method not allowed")
else:
    n=0
    while n<0:
        c=(a+b)/2
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
            n=n+1
        print("root of given equation= ", c)



# ----------< x**2 -4 >---------

# def f(x):
#     return x**2 - 4

# a = 1.0
# b = 3.0
# tolerance = 0.0001
# max_iterations = 100

# if f(a) * f(b) >= 0:
#     print("Invalid interval: no sign change.")
# else:
#     for i in range(max_iterations):
#         c = (a + b) / 2

#         print(f"Iteration {i + 1}: c = {c:.6f}")

#         if abs(f(c)) < tolerance:
#             break

#         if f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c

#     print("Approximate root =", round(c, 6))
