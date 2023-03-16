import requests as req
from tkinter import *

group_message_id_list = []
private_message_id_list = []

with open(file='black_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        blacklist = list(f.readlines())
        blacklist = blacklist[0][1:-1].split(',')
        for temp in range(len(blacklist)):
            blacklist[temp] = int(blacklist[temp])
    except (IndexError, ValueError):
        blacklist = []
    finally:
        f.close()
with open(file='admin_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        adminlist = list(f.readlines())
        adminlist = adminlist[0][1:-1].split(',')
        for temp in range(len(adminlist)):
            adminlist[temp] = int(adminlist[temp])
    except (IndexError, ValueError):
        adminlist = []
    finally:
        f.close()
with open(file='can_use_python_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        python_list = list(f.readlines())
        python_list = python_list[0][1:-1].split(',')
        for temp in range(len(python_list)):
            python_list[temp] = int(python_list[temp])
    except (IndexError, ValueError):
        python_list = []
    finally:
        f.close()
with open(file='chat_gpt_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        chat_gpt_list = list(f.readlines())
        chat_gpt_list = chat_gpt_list[0][1:-1].split(',')
        for temp in range(len(chat_gpt_list)):
            chat_gpt_list[temp] = int(chat_gpt_list[temp])
    except (IndexError, ValueError):
        chat_gpt_list = []
    finally:
        f.close()
with open(file='summon_images_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        summon_images_list = list(f.readlines())
        summon_images_list = summon_images_list[0][1:-1].split(',')
        for temp in range(len(summon_images_list)):
            summon_images_list[temp] = int(summon_images_list[temp])
    except (IndexError, ValueError):
        summon_images_list = []
    finally:
        f.close()
with open(file='group_admin_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        group_admin_list = list(f.readlines())
        group_admin_list = group_admin_list[0][1:-1].split(',')
        for temp in range(len(group_admin_list)):
            group_admin_list[temp] = int(group_admin_list[temp])
    except (IndexError, ValueError):
        group_admin_list = []
    finally:
        f.close()
with open(file='can_use_java_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        java_list = list(f.readlines())
        java_list = java_list[0][1:-1].split(',')
        for temp in range(len(java_list)):
            java_list[temp] = int(java_list[temp])
    except (IndexError, ValueError):
        java_list = []
    finally:
        f.close()
with open(file='can_use_c_list.txt', mode='r+', encoding='utf-8') as f:
    try:
        c_list = list(f.readlines())
        c_list = c_list[0][1:-1].split(',')
        for temp in range(len(c_list)):
            c_list[temp] = int(c_list[temp])
    except (IndexError, ValueError):
        c_list = []
    finally:
        f.close()


def send_group_message(group, message):
    global group_message_id_list
    message = req.get('http://127.0.0.1:5700/send_group_msg?group_id={}&message={}'.format(group, message))
    group_message_id_list.append(eval(message.content.decode())['data']['message_id'])
    print(group_message_id_list)


def send_private_message(user_id, message):
    global private_message_id_list
    message = req.get('http://127.0.0.1:5700/send_private_msg?user_id={}&message={}'.format(user_id, message))
    private_message_id_list.append(eval(message.content.decode())['data']['message_id'])
    print(private_message_id_list)


def delete_group_message():
    global group_message_id_list
    req.get(
        'http://127.0.0.1:5700/delete_msg?message_id={}'.format(group_message_id_list[len(group_message_id_list) - 1]))
    del group_message_id_list[len(group_message_id_list) - 1]


def delete_private_message():
    global private_message_id_list
    req.get('http://127.0.0.1:5700/delete_msg?message_id={}'.format(
        private_message_id_list[len(private_message_id_list) - 1]))
    del private_message_id_list[len(private_message_id_list) - 1]


def create():
    window = Tk()
    window.title('机器人管理器')
    window.geometry('500x500')

    def send_group_msg():
        entry_get = entry.get()
        entry_get1 = entry1.get()
        send_group_message(entry_get, entry_get1)

    def send_private_msg():
        entry_get = entry.get()
        entry_get1 = entry1.get()
        send_private_message(entry_get, entry_get1)

    def blacklist_append():
        blacklist.append(int(entry2.get()))
        with open(file='black_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(blacklist))
            f.close()

    def blacklist_remove():
        blacklist.remove(int(entry2.get()))
        with open(file='black_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(blacklist))
            f.close()

    def adminlist_append():
        adminlist.append(int(entry2.get()))
        with open(file='admin_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(adminlist))
            f.close()

    def adminlist_remove():
        adminlist.remove(int(entry2.get()))
        with open(file='admin_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(adminlist))
            f.close()

    def python_append():
        python_list.append(int(entry2.get()))
        with open(file='can_use_python_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(python_list))
            f.close()

    def python_remove():
        python_list.remove(int(entry2.get()))
        with open(file='can_use_python_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(python_list))
            f.close()

    def chat_append():
        chat_gpt_list.append(int(entry2.get()))
        with open(file='chat_gpt_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(chat_gpt_list))
            f.close()

    def chat_remove():
        chat_gpt_list.remove(int(entry2.get()))
        with open(file='chat_gpt_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(chat_gpt_list))
            f.close()

    def image_append():
        summon_images_list.append(int(entry2.get()))
        with open(file='summon_images_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(summon_images_list))
            f.close()

    def image_remove():
        summon_images_list.remove(int(entry2.get()))
        with open(file='summon_images_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(summon_images_list))
            f.close()

    def group_append():
        group_admin_list.append(int(entry2.get()))
        with open(file='group_admin_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(group_admin_list))
            f.close()

    def group_remove():
        group_admin_list.remove(int(entry2.get()))
        with open(file='group_admin_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(group_admin_list))
            f.close()

    def java_append():
        java_list.append(int(entry2.get()))
        with open(file='can_use_java_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(java_list))
            f.close()

    def java_remove():
        java_list.remove(int(entry2.get()))
        with open(file='can_use_java_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(java_list))
            f.close()

    def c_append():
        c_list.append(int(entry2.get()))
        with open(file='can_use_c_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(c_list))
            f.close()

    def c_remove():
        c_list.remove(int(entry2.get()))
        with open(file='can_use_c_list.txt', mode='w+', encoding='utf-8') as f:
            f.write(str(c_list))
            f.close()

    label = Label(window, text='群（QQ号）')
    label.place(relheight=0.1, relwidth=0.2, relx=0.1, rely=0)

    label1 = Label(window, text='消息内容')
    label1.place(relheight=0.1, relwidth=0.2, relx=0.1, rely=0.1)

    label2 = Label(window, text='值')
    label2.place(relheight=0.1, relwidth=0.1, relx=0.1, rely=0.4)

    entry = Entry(window)
    entry.place(relheight=0.1, relwidth=0.7, relx=0.3, rely=0)

    entry1 = Entry(window)
    entry1.place(relheight=0.1, relwidth=0.7, relx=0.3, rely=0.1)

    entry2 = Entry(window)
    entry2.place(relheight=0.1, relwidth=0.7, relx=0.2, rely=0.4)

    button = Button(window, text='发送（私聊）', command=send_private_msg)
    button.place(relheight=0.1, relwidth=0.2, relx=0.7, rely=0.3)

    button1 = Button(window, text='发送（群聊）', command=send_group_msg)
    button1.place(relheight=0.1, relwidth=0.2, relx=0.7, rely=0.2)

    button2 = Button(window, text='撤回（私聊）', command=delete_private_message)
    button2.place(relheight=0.1, relwidth=0.2, relx=0.1, rely=0.2)

    button3 = Button(window, text='黑名单（添加）', command=blacklist_append)
    button3.place(relheight=0.1, relwidth=0.2, relx=0, rely=0.5)

    button4 = Button(window, text='黑名单（删除）', command=blacklist_remove)
    button4.place(relheight=0.1, relwidth=0.2, relx=0.2, rely=0.5)

    button5 = Button(window, text='管理员（添加）', command=adminlist_append)
    button5.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.5)

    button6 = Button(window, text='管理员（删除）', command=adminlist_remove)
    button6.place(relheight=0.1, relwidth=0.2, relx=0.6, rely=0.5)

    button7 = Button(window, text='python（添加）', command=python_append)
    button7.place(relheight=0.1, relwidth=0.2, relx=0.8, rely=0.5)

    button8 = Button(window, text='python（删除）', command=python_remove)
    button8.place(relheight=0.1, relwidth=0.2, relx=0, rely=0.6)

    button9 = Button(window, text='chat（添加）', command=chat_append)
    button9.place(relheight=0.1, relwidth=0.2, relx=0.2, rely=0.6)

    button10 = Button(window, text='chat（删除）', command=chat_remove)
    button10.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.6)

    button11 = Button(window, text='image（添加）', command=image_append)
    button11.place(relheight=0.1, relwidth=0.2, relx=0.6, rely=0.6)

    button12 = Button(window, text='image（删除）', command=image_remove)
    button12.place(relheight=0.1, relwidth=0.2, relx=0.8, rely=0.6)

    button13 = Button(window, text='group（添加）', command=group_append)
    button13.place(relheight=0.1, relwidth=0.2, relx=0, rely=0.7)

    button14 = Button(window, text='group（删除）', command=group_remove)
    button14.place(relheight=0.1, relwidth=0.2, relx=0.2, rely=0.7)

    button15 = Button(window, text='java（添加）', command=java_append)
    button15.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.7)

    button16 = Button(window, text='java（删除）', command=java_remove)
    button16.place(relheight=0.1, relwidth=0.2, relx=0.6, rely=0.7)

    button17 = Button(window, text='c（添加）', command=c_append)
    button17.place(relheight=0.1, relwidth=0.2, relx=0.8, rely=0.7)

    button18 = Button(window, text='c（删除）', command=c_remove)
    button18.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.8)

    button19 = Button(window, text='撤回（群聊）', command=delete_private_message)
    button19.place(relheight=0.1, relwidth=0.2, relx=0.1, rely=0.3)

    window.mainloop()


if __name__ == '__main__':
    create()
