import datetime
import json

def main():
    journal_file = './data/journal.json'

    banner()
    run_event_loop(journal_file)


def banner():
    print('-----------------------------------')
    print('---       My Journal Practice   ---')
    print('-----------------------------------')

def menu():
    user_choice = input("Would you like to [A]dd, [L]ist journal entries or E[x]it: ").lower().strip()
    return user_choice

def run_event_loop(journal_file):

    # set to False for init value of loop
    menu_entry = False

    # journal data, empty dict until we get json added.

    journal_data = open_journal(journal_file)

    while menu_entry != 'x':
        menu_entry = menu()

        if menu_entry == 'a':
            # Add a item
            journal_data = entry_add(journal_data)
            write_journal(journal_data,journal_file)
        elif menu_entry == 'l':
            # list entries
            entry_list(journal_data)
        elif menu_entry != 'x':
            print('Sorry but {} is not a choice at this time please choose again'.format(menu_entry))



def entry_add(data):
    entry_title = input('Enter title for your entry: ')
    entry_text = input('Enter {} data: '.format(entry_title))
    entry_date = datetime.datetime.now()
    data[entry_title] = {
        'text': entry_text,
        'date': entry_date
    }
    return data

def entry_list(data):
    for idx,key in enumerate(data):
        # add one to index for humans
        print(str(idx +1 ) + ": "  + key)

def open_journal(jfile):
    # open the file, create if not present
    data = {}

    try:
        with open(jfile, 'r+') as input:
            data = json.load(input)
    except OSError:
        print('Unable to open file {}'.format(jfile))

    return data

def write_journal(data,jfile):
    try:
        with open(jfile, 'w') as outfile:
           json.dump(data, outfile, sort_keys=True, indent=4, default=str )
    except OSError:
        print('Unable to open file {}'.format(jfile))


if __name__ == '__main__':
    main()
