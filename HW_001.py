a = int(input("Введите целое число: "))
num = a

ratio = ""
res = []

divisors = [16]

for i in divisors:
    while num > 0:
        if num % i <= 9:
            ratio += f"{num % i}"
            num //= i
        else:
            x = num % i
            match x:
                case 10:
                    ratio += "a"
                    num //= i
                case 11:
                    ratio += "b"
                    num //= i
                case 12:
                    ratio += "c"
                    num //= i
                case 13:
                    ratio += "d"
                    num //= i
                case 14:
                    ratio += "e"
                    num //= i
                case 15:
                    ratio += "f"
                    num //= i
    print(f"Введенное число в {i}-й системе равно: " + "".join(reversed(ratio)))  # Еще можно использовать срез [::-1]
    ratio = []
    num = a

print(*res)
print(hex(a)[2:])  # Срез для красоты, убираем "0b"
