import os
import csv

def count_rows(csv_file):
    with open(csv_file, 'r', encoding='utf-8', newline='') as file:
        return sum(1 for row in csv.DictReader(file) if row.get('ID') and row['ID'].strip().isdigit())

def find_messages_folder(starting_dir):
    return next((os.path.join(root, 'messages') for root, dirs, files in os.walk(starting_dir) if 'messages' in dirs), None)

def process_csv_files(script_dir):
    messages_dir = find_messages_folder(script_dir)

    if messages_dir:
        total = sum(count_rows(os.path.join(root, file)) for root, dirs, files in os.walk(messages_dir) for file in files if file.endswith('.csv'))
        print(f"You have {total} messages in total.")
    else:
        print("The 'messages' folder was not found :c")

def basic_info(script_dir):
    messages_dir = find_messages_folder(script_dir)

    if messages_dir:
        channel_count = sum(1 for name in os.listdir(messages_dir) if os.path.isdir(os.path.join(messages_dir, name)))
        print(f"You have written in {channel_count} channels which includes DMs")
    else:
        print("The 'messages' folder was not found :c")

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Menu:")
        print("1. Tells you how many channels you have wrote in (includes DMs)")
        print("2. Tells you how many messages you have in total")
        print("Q. Quit")

        choice = input("Tell me which (1, 2, or Q): ")

        if choice == '1':
            basic_info(script_dir)
        elif choice == '2':
            process_csv_files(script_dir)
        elif choice.upper() == 'Q':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or Q.")
        
        input("Press Enter to continue")

    input("Press Enter to exit")

if __name__ == "__main__":
    main()
