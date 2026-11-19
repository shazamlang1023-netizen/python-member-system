names = ["小明", "小華", "小美", "小王", "小林"]

print(names[0])
print(names[1])
print(names[2])

names = ["小明", "小華", "小美", "小王", "小林"]
names.append("小李")
print(names)

names = ["小明", "小華", "小美", "小王", "小林"]
names.remove("小美")
print(names)

names = ["小明", "小華", "小美", "小王", "小林"]
for name in names:
    print(name)

user = {
    "name": "小明",
    "age": 18,
    "email": "test@example.com"
}
print(user)

print(user["name"])
print(user["age"])

user["age"] =28
print(user["age"])

user['phone'] = "0976473232"
print(user)


members = []

def add_member():
    name = input("請輸入會員姓名：")
    age = int(input("請輸入會員年齡："))
    member = {
        "name": name,
        "age": age
    }
    members.append(member)
    print("會員已新增！")

def delete_member():
    name = input("請輸入要刪除的會員姓名：")
    for member in members:
        if member["name"] == name:
            members.remove(member)
            print("會員已刪除！")
            return
    print("找不到該會員！")

def show_members():
    if not members:
        print("目前沒有會員。")
    else:
        print("會員列表：")
        for member in members:
            print(f"姓名：{member['name']}, 年齡：{member['age']}")

while True:
    print("\n===== 會員管理系統 =====")
    print("1. 新增會員")
    print("2. 顯示會員列表")
    print("3. 刪除會員")
    print("4. 離開系統")

    choice = input("請輸入選項：")

    if choice == "1":
        add_member()
    elif choice == "2":
        show_members()
    elif choice == "3":
        delete_member()
    elif choice == "4":
        print("感謝使用會員管理系統！")
        break
    else:
        print("無效的選項，請重新輸入。")