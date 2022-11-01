first_name = ''
last_name = ''
age = ''
dest = ''


def data_retrieve():
    global first_name
    first_name = input('Enter your first name ')
    global last_name
    last_name = input('Enter your last name ')
    global age
    age = input('Enter your age ')
    global dest
    dest = input('Enter your destination ')


def data_process():
    result = "Name: " + first_name[0] + "." + last_name + "," + age + "\nDestination: " + dest
    return result


def ticket_print():
    data_retrieve()
    print(data_process())


ticket_print()
