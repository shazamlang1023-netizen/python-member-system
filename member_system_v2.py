import json
import os

FILE_NAME = "members.json"

#讀取會員資料
def load_members():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

#儲存會員資料
def save_members(members):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(members, file, ensure_ascii=False, indent=4)

        members = load_members()

        print("目前會員資料:")
        print(members)

#新增會員
def add_member():
    name = input("請輸入會員姓名：")
    age = int(input("請輸入會員年齡："))
    member = {
        "name": name,
        "age": age
    }
    members.append(member)
    save_members(members)
    print("會員已新增！資料已儲存。")


# 查看會員列表
def show_members():
    print("\n==== 會員列表 ====")

    for member in members:
        print(f"姓名：{member['name']}, 年齡：{member['age']}")
        print("--------")

#刪除會員
def delete_member():
    name = input("請輸入要刪除的會員姓名：")
    for member in members:
        if member["name"] == name:
            members.remove(member)
            save_members(members)
            print("會員已刪除！資料已儲存。")
            return
    print("找不到該會員！")

#載入會員資料
members = load_members()

#主選單
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
    