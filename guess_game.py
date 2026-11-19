answer = 7

while True:
    guess = int(input("請猜一個 1 到 10 的數字："))

    if guess == answer:
        print("恭喜你，猜對了！")
        break
    elif guess < answer:
        print("太小了，再試一次！")
    else:
        print("太大了，再試一次！")
