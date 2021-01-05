# ----------------------------->>> Comparison Operators <<<-----------------------------
a = 3
print(a == a)
print(a != a)
print(a > a)
print(a < a)
print(a >= a)
print(a <= a)
# ---------------------------->>> Conditional Expressions <<<---------------------------
a = 5
b = 2
if a >= b:
    print("a is greater than b")
else:
    print("b is greater than a")
# -------------------------->>> Basic operators <<<-----------------------
# Arithmetic operators
a = 2
print(a+a)
print(a-a)
print(a*a)
print(a/a)
print(a % a)
print(a**a)
print(a//a)
# Assignment operators
a = 5
print(a)
# a = a+2 same for all
a += 2
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)
a %= 2
print(a)
a = 5
a **= 2
print(a)
a //= 2
print(a)
# Bitewise operators
a = 5
a &= 2
print(a)
a = 5
a |= 2
print(a)
a = 5
a ^= 2
print(a)
a = 5
a >>= 2
print(a)
a = 5
a <<= 2
print(a)
# Logical Operators
print(a <= a and a >= a)
print(a == a or a > a)
print(not(a <= a and a >= a))
# Identity Operatos
my_friends = ["MH", "Gul", "Sultan"]
x = my_friends
print(x is my_friends)
print(x is not my_friends)
# Membership Operators
print("MH" in my_friends)
print("Gul" not in my_friends)


# ----------------------------->>> Chained Operators <<<-------------------------------
a = 3
b = 5
c = 15
print(a < b < c)
print(a <= b <= c)
print(a < b*c/a % b//c)
