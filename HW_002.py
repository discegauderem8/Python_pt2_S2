from fractions import Fraction
import math


def getmult(fractions_parts):
    numerator = 1
    nominator = 1

    for i in fractions_parts:
        numerator *= int(i[0])
        nominator *= int(i[1])

    gcd = math.gcd(numerator, nominator)

    if gcd > 1:
        numerator //= gcd
        nominator //= gcd

    return f"{numerator}/{nominator}"


def getsum(fractions_parts):
    numerator = 0
    nominator = 1

    if fractions_parts[0][1] != fractions_parts[1][1]:
        nominator = max(int(fractions_parts[0][1]), int(fractions_parts[1][1]))
        for i in (fractions_parts):
            numerator += int(i[0]) * nominator//int(i[1])

    gcd = math.gcd(numerator, nominator)

    if gcd > 1:
        numerator //= gcd
        nominator //= gcd

    return f"{numerator}/{nominator}"


a = input("Введите 1-ю дробь в формате a/b: ")
b = input("Введите 2-ю дробь в формате a/b: ")

my_fractions_parts = [(a.split("/")), (b.split("/"))]

print(f"Произведение дробей: {getmult(my_fractions_parts)}")
print(f"Сумма дробей: {getsum(my_fractions_parts)}")

print()

frac1 = Fraction(int(my_fractions_parts[0][0]), int(my_fractions_parts[0][1]))
frac2 = Fraction(int(my_fractions_parts[1][0]), int(my_fractions_parts[1][1]))

print(frac1 * frac2)
print(frac1 + frac2)
