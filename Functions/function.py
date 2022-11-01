def basic_function():
    print("Hello World!")


basic_function()


def greet():
    name = input("Enter your name ")
    print("Hello " + name)


greet()


def name_input():
    name_list = []
    name = ''
    while name != 'STOP':
        name_list.append(name)
        name = input('Enter Name, type STOP to end ')
    return name_list


def name_process():
    fin_list = name_input()
    count = 0
    while count != len(fin_list):
        print(fin_list[count])
        count = count + 1


name_process()
