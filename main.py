def check_binary(num: str) -> bool:
    return all(ch in "01" for ch in num)

def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]

def sub_binary(a: str, b: str) -> str:
    if int(a, 2) < int(b, 2):
        return "Помилка: результат від’ємний"
    return bin(int(a, 2) - int(b, 2))[2:]

def mul_binary(a: str, b: str) -> str:
    return bin(int(a, 2) * int(b, 2))[2:]

def div_binary(a: str, b: str):
    if b == "0":
        return "Помилка: ділення на нуль"
    q = int(a, 2) // int(b, 2)
    r = int(a, 2) % int(b, 2)
    return f"Частка: {bin(q)[2:]}, залишок: {bin(r)[2:]}"

the_end = False
while not the_end:
    a = input("Введіть перше двійкове число: ")
    if not check_binary(a):
        print("Помилка! Це не двійкове число.")
        continue

    op = input("Введіть операцію (+, -, *, /): ")
    if op not in {"+", "-", "*", "/"}:
        print("Помилка! Невідома операція.")
        continue

    b = input("Введіть друге двійкове число: ")
    if not check_binary(b):
        print("Помилка! Це не двійкове число.")
        continue

    if op == "+":
        print("Результат:", add_binary(a, b))
    elif op == "-":
        print("Результат:", sub_binary(a, b))
    elif op == "*":
        print("Результат:", mul_binary(a, b))
    elif op == "/":
        print("Результат:", div_binary(a, b))

    ask_to_continue = input("Бажаєте продовжити? (так/ні): ").lower()
    if ask_to_continue == "ні":
        the_end = True