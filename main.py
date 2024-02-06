import os
import pickle
from datetime import datetime
from collections import UserDict


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __str__(self):
        return str(self.__value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        Field.__init__(self, value)
        if value.isdigit() and len(value) == 10:
            pass
        else:
            raise ValueError('The phone number is in the wrong format!')


class Birthday(Field):
    def __init__(self, value):
        Field.__init__(self, value)
        if bool(datetime.strptime(str(value), '%d.%m.%Y')):
            pass


class Record:
    def __init__(self, name, day_birthday=None):
        self.name = Name(name)
        self.phones = []
        self.day_birthday = Birthday(day_birthday) if day_birthday else None


    def add_phone(self, num):
        self.phones.append(Phone(num))
        return self.phones


    def remove_phone(self, num):
        for i, phone in enumerate(self.phones):
            if num == phone.value:
                del self.phones[i]


    def edit_phone(self, old_num, new_num):
        for i, phone in enumerate(self.phones):
            if old_num == phone.value:
                self.phones[i] = Phone(new_num)
                return self.phones
        raise ValueError('This phone does not exist')


    def find_phone(self, num):
        for phone in self.phones:
            if num == phone.value:
                return Phone(num)
        return None

    def days_to_birthday(self):
        today = datetime.now().date()
        birth = datetime.strptime(str(self.day_birthday), '%d.%m.%Y').date()
        birth = birth.replace(year=today.year)
        if birth == today:
            return 0
        else:
            if birth < today:
                birth = birth.replace(year=today.year + 1)
                return birth - today

            return birth - today


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        UserDict.__init__(self)
        self.dir_file = "data.txt"
        self.data = {} if self.file_created() else self.load_pickle()


    def file_created(self):
        if os.path.exists(self.dir_file) and os.path.getsize(self.dir_file) > 0:
            return False
        return True

    def add_record(self, args):
        self.data[args.name.value] = args
        return self.data


    def find(self, name):
        if name in self.data:
            return self.data[name]


    def delete(self, name):
        self.data.pop(name, 'No Key found')


    def iterator(self, num):
        i = 0
        while i < len(self.data):
            yield list(self.data.items())[i:i+num]
            i += num

    def write_pickle(self):

        with open(self.dir_file, 'wb') as file:
            pickle.dump(self.data, file)


    def load_pickle(self):
        with open(self.dir_file, 'rb') as file:
            self.data = pickle.load(file)
            return self.data


    def have_matches(self, matc):
        list_users = []
        for contact in self.iterator(1):
            print(contact, '???')
            if matc in contact[0]:
                list_users.append(contact)
        return list_users


#print(self.data == data_loaded)


if __name__ == "__main__":
    ...
    # # Створення нової адресної книги
    # book = AddressBook()

    # # Створення запису для John
    # john_record = Record("John", '20.06.1987')
    # john_record.add_phone("1234567890")
    # john_record.add_phone("5555555555")
    # book.add_record(john_record)

    # # Створення та додавання нових записів дляперевірки ітератора
    # for i in range(10):
    #     john_record = Record('John'+str(i))
    #     john_record.add_phone("123456789"+str(i))
    #     book.add_record(john_record)

    # print(book.have_matches('oh'))

    # # Запис і читання з файлу за допомогою pickle
    # book.write_pickle()
    # book.load_pickle()

    # Виведення записів через ітератор
    # itr = book.iterator(4)
    # for i in itr:
    #     print(i)

    # # Кількість днів до дня народження
    # print(john_record.days_to_birthday())


    # Додавання запису John до адресної книги
    #book.add_record(john_record)

    # # Створення та додавання нового запису для Jane
    # jane_record = Record("Jane")
    # jane_record.add_phone("9876543210")
    # book.add_record(jane_record)

    # # Виведення всіх записів у книзі
    # for name, record in book.data.items():
    #     print(record)

    # # Знаходження та редагування телефону для John
    # john = book.find("John")
    # john.edit_phone("1234567890", "1112223333")

    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
    # book.delete("Jane")
    