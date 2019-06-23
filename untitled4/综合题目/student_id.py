dic = {}
while True:
    name = input("请输入姓名：")
    id = input("请输入学号：")
    dic[name] = id
    if input("还要继续输入吗？") == "n":
        break

while True:
    check = str(input("请输入待查找的姓名或学号：('n'退出）"))
    if check == "n":
        break
    for key, value in dic.items():
        if check == key or check == str(value):
            if check == key:
                print("学号为：" + str(dic[key]))
            if check == str(value):
                print("姓名为：" + str(key))
        break
    else:
        print("不存在")
