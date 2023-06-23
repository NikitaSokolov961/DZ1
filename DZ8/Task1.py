file_path = "file.txt"


def show_all_records():
    with (open(file_path, 'r', encoding="utf-8")) as _data:
        for i, line in enumerate(_data, 1):
            phonebook_data = line.replace(";", " ")
            print(i, phonebook_data, end="")


def search_record(name):
    with (open(file_path, 'r', encoding="utf-8")) as _data:
        for line in _data:
            if name in line:
                print(line)
                return
    print("Контакт не найден")


def add_contact(new_contact_fio, new_contact_number):
    with (open(file_path, 'a', encoding="utf-8")) as f:
        f.write("\n")
        f.write(new_contact_fio.replace(" ",";"))
        f.write(';')
        f.write(new_contact_number)


def edit_contact(number, fio, phone):
    with (open(file_path, 'r', encoding="utf-8")) as f:
        data = list(f.readlines())
        data[number - 1] = fio.replace(" ", ";") + ";" + str(phone)
        if number < len(data):
            data[number - 1] += "\n"
    with (open(file_path, 'w', encoding="utf-8")) as f:
        f.writelines(data)


def delete_contact(number):
    with (open(file_path, 'r', encoding="utf-8")) as f:
        data = list(f.readlines())
        if number > len(data):
            print("Недоступный метод строки")
            return
        del data[number - 1]
    with (open(file_path, 'w', encoding="utf-8")) as f:
        f.writelines(data)


def main():
    while True:
        print("\nВыберите действие "
              "\n1 - Вывести все записи "
              "\n2 - найти контакт "
              "\n3 - добавить контакт "
              "\n4 - редактировать контакт "
              "\n5 - удалить контакт "
              "\n6 - выход ")
        select = int(input())
        if select == 1:
            show_all_records()
        elif select == 2:
            name = input("Введите Имя или Фамилию: ")
            search_record(name)
        elif select == 3:
            fio = input("Введите ФИО через пробел: ")
            number = input("Введите номер: ")
            add_contact(fio, number)
        elif select == 4:
            show_all_records()
            number = int(input("\nВведите номер строки для редактирования: "))
            fio = input("Введите ФИО через пробел: ")
            phone = input("Введите номер телефона: ")
            edit_contact(number, fio, phone)
        elif select == 5:
            show_all_records()
            number = int(input("\nВведите номер строки для удаления: "))
            delete_contact(number)
        elif select == 6:
            break

main()