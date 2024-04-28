'''
Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

Вимоги до завдання:

Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.
'''
#decorator func
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f'ValueError: {e}'
        except KeyError as e:
            return f"KeyError: {e}"
        except IndexError as e:
            return f"IndexError: {e}"
        

    return inner


@input_error
#Function that show all contacts.
def show_all(contacts):
    return contacts


@input_error
#Function that show Phone number by users name.
def show_phone(args, contacts):
    if args:
        name = args[0]
        if name in contacts: #Check if we have this contact in the dictionary
            return contacts[name]
        else:
            raise KeyError("This contacts is not exist, use 'add' command to create a new one")
    else:
        return f'User name was not provided' 


@input_error
#Function that change a phone number by users name.   
def change_contact(args, contacts):
    if len(args) < 2: #check if we have all arguments to work with from the list
        raise ValueError('To change the contact you need to provide name that exist in phonebook and a new phone')

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f'Contact updated.'


@input_error
def parse_input(user_input):    
        user_input = user_input.strip() 
        cmd, *args = user_input.split()
        cmd = cmd.lower()
        return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) < 2: #check if we have all arguments to work with from the list
        raise ValueError('To add the number you need to provide a name and a personal phone')
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
