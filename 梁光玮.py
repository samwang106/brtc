from time import sleep
print("|--欢迎进入通讯录程序--|")
sleep(0.5 )
print("|-- 1:查询联系人资料 --|")
sleep(0.5)
print("|-- 2:插入新的联系人 --|")
sleep(0.5)
print("|-- 3:删除已有联系人 --|")
sleep(0.5)
print("|-- 4:退出通讯录程序 --|")
sleep(0.5)

dict1 = {}

a = 1
while a>0:
    num = input('请输入相关的指令代码：')
    if num == '1':
        name = input('请输入联系人姓名：')
        if name not in dict1:
            print('您输入的姓名不在通讯录中！')
        else:
            print(dict1[name])
    if num == '2':
        name = input('请输入联系人姓名：')
        if name in(dict1):
            print('您输入的联系人已在通讯录中！')
        else:
            dict1[name] = input('请输入联系人电话：')
            print(dict1)
    if num == '3':
        name = input('请输入联系人姓名：')
        if name not in(dict1):
            print('您输入的联系人不在通讯录中！')
        else:
            del(dict1[name])
            print('已删除该联系人！')
            print(dict1)
    if num == '4':
        print('|--感谢使用通讯录程序--|')
        a = a-1
    if num not in('1','2','3','4'):
        print('请输入1-4的代码操作！')
    
        
    
