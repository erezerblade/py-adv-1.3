class Contact:
    def __init__(self, f_name, l_name, phone, *args, **kwargs):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.favorite = None
        self.additional_info = []
        for favorite in args:
            self.favorite = favorite
        for add_info_name, add_info_value in kwargs.items():
            self.additional_info.append(f'{add_info_name}: {add_info_value}')
        self.list_adds = '\n'.join(self.additional_info)

    def __str__(self):
        return f'Имя: {self.f_name}\n' \
               f'Фамилия: {self.l_name}\n' \
               f'Телефон: {self.phone}\n' \
               f'В избранных: {self.favorite}\n' \
               f'Дополнительная информация:\n{self.list_adds}'


class PhoneBook:
    def __init__(self, name):
        self.book_name = name
        self.contacts = []

    def print_contacts(self):
        for i in self.contacts:
            print('===========')
            print(i)
        pass

    def add_contact(self, f_name, l_name, phone, *args, **kwargs):
        contact = Contact(f_name, l_name, phone, *args, **kwargs)
        self.contacts.append(contact)
        pass

    def delete_number(self, number):
        for i in self.contacts:
            if number in i.phone:
                self.contacts.remove(i)
        pass

    def get_favorites(self):
        for i in self.contacts:
            if i.favorite:
                print('===========')
                print(i)
        pass

    def get_contact(self, name):
        for contact in self.contacts:
            if name == contact.f_name:
                print('===========')
                print(contact)
            elif name == contact.l_name:
                print('===========')
                print(contact)
        pass


# =========================================================================================================
MyPhoneBook = PhoneBook("Черная Книжечка")

if __name__ == '__main__':
    # Добавление и вывод
    MyPhoneBook.add_contact('John', 'Smith', '+71234567809', 'да', telegram='@johny', email='johny@smith.com')
    MyPhoneBook.add_contact('Simon', 'Templar', '+73214567809', telegram='@simon', email='simon@templar.com')
    MyPhoneBook.add_contact('Jenny', 'Smith', '+71236547809', telegram='@jenny', email='jenny@smith.com')
    MyPhoneBook.add_contact('Simona', 'Templar', '+73216547809', 'да', telegram='@simona', email='simona@templar.com')
    MyPhoneBook.print_contacts()

    # Удаление и вывод
    MyPhoneBook.delete_number('+73216547809')
    MyPhoneBook.print_contacts()

    # Вывод избранных контактов
    MyPhoneBook.get_favorites()

    # Поиск по имени и фамилии
    MyPhoneBook.get_contact("Jenny")