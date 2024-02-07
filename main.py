''' Консольний бот помічник '''

import main_class

book = main_class.AddressBook()

def input_error(func):
    ''' Декоратор '''
    def inner(*args):
        try:
            return func(*args)
        except (IndexError, KeyError, ValueError):
            return 'Name or Number not correct!'
    return inner


def main():
    ''' Функція обробки введення виведення '''
    book.file_created()
    print(book.data)
    while True:
        comand_list = input('Input you comand: ')
        comand = comand_list.lower().split()
        contact = main_class.Record(comand[1]) if len(comand)>1 else None
        result = handler(comand_list)(comand, contact)
        print(result)
        if result == "Good bye!":
            break


@input_error
def handler(comand_list):
    ''' Функція обробки введених данних '''
    comand = comand_list.lower().split()
    if comand_list == '':
        return lambda *_: 'Correct the input!!! The entered command is empty!!!'
    if len(comand) > 3:
        return lambda *_: 'You comand is very long'
    if len(comand) == 2:
        if comand[0] == 'good' and comand[1] == 'bye' or\
           comand[0] == 'show' and comand[1] == 'all':
            return OPERATIONS[comand_list]
    if comand[0] in OPERATIONS:
        return OPERATIONS[comand[0]]
    return lambda *_: f'Correct the input!!! The entered command <{comand}> is not valid!!!'

@input_error
def handler_hello(*_):
    return 'How can I help you?'


@input_error
def handler_add(comand, contact):
    contact.add_phone(comand[2])
    book.add_record(contact)
    return f'A new contact {comand[1]} has been created.'


@input_error
def handler_change(comand, contact):
    contact.add_phone(comand[2])
    book.add_record(contact)
    return f'A new number has been recorded {comand[2]}.'


@input_error
def handler_phone(comand, contact):
    return contact.find_phone(comand[2])


@input_error
def handler_show(*_):
    return f'Oll list of telephone book: {[record for name, record in book.data.items()]}'


@input_error
def handler_exit(*_):
    book.write_pickle()
    return "Good bye!"


OPERATIONS = {
    'hello': handler_hello, 'add': handler_add, 'change': handler_change, 'phone': handler_phone,
    'show all': handler_show, 'good bye': handler_exit, 'close': handler_exit, 'exit': handler_exit,
}

main()
