from src.reminder import PoliteReminder
from src.deadlined_reminders import DeadlinedReminder
from src.database import add_reminder, list_reminders
from src.external_reminders import EveningReminder

DeadlinedReminder.register(PoliteReminder)


def handle_input():
    choice = input("Choice: ")
    if choice == "3":
        return False

    if(choice == "1"):
        list_reminders()

    elif(choice == "2"):
        print()
        reminder = input("What would you like to be reminded about?: ")
        date = input("When is the due?: ")
        # if issubclass(EveningReminder, DeadlinedReminder):
        add_reminder(reminder, date, PoliteReminder)
        list_reminders()
    else:
        print("Invalid menu option")

    return True


def print_menu():
    print('1) List reminders')
    print('2) Add a reminder')
    print('3) Exit')


def main():
    print_menu()
    while handle_input():
        print_menu()


if __name__ == '__main__':
    main()
