def say_hello():
    print("你好！")
    print("歡迎學習 Python！")

say_hello()

def add(a, b):
    result = a + b
    print(result)

add(10, 20)
add(100, 200)
add(5, 8)

def add(a, b):
    return a + b

total = add(100, 200)

print(total)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "不能除以 0"
    return a / b


print("===== Python 計算機 =====")

num1 = float(input("請輸入第一個數字："))
num2 = float(input("請輸入第二個數字："))

print("加法結果：", add(num1, num2))
print("減法結果：", subtract(num1, num2))
print("乘法結果：", multiply(num1, num2))
print("除法結果：", divide(num1, num2))