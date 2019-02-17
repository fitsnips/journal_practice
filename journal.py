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
    user_choice = input("Would you like to [A]dd, [L]ist, [R]emove, [P]rint, [U]pdate journal entries or E[x]it: ").lower().strip()
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
        elif menu_entry == 'r':
            # remove entry
            entry_remove(journal_data)
            write_journal(journal_data,journal_file)
        elif menu_entry == 'p':
            # print the text of the entry
            entry_print(journal_data)
        elif menu_entry == 'u':
            # update text of entry
            entry_update(journal_data)
            write_journal( journal_data, journal_file)
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
    # keep a key to number index, for human interaction
    data_index = []

    if not data:
        print('Journal is empty')
        return

    for idx,entry in enumerate(data):
        data_index.append(entry)
    for count,key in enumerate(data_index):
        print(str(count +1) + ": " + key)

    return data_index

def entry_remove(data):
    data_index = entry_list(data)
    remove_item = input('Which item number would you like to remove: ')
    remove_key = data_index[int(remove_item) - 1]
    try:
        del data[remove_key]
    except KeyError:
        print('Journal removal error, key {} not present'.format(idx + 1))
    return data

def entry_print(data):
    entry_index = entry_list(data)
    if len(entry_index) == 0:
        print('Journal is empty')
        return

    selected_entry = input('Which entry would you like to view: ')
    print()
    printed_entry = entry_index[int(selected_entry) - 1]
    print('Entry {} contains the following text: '.format(printed_entry))
    print(str(data[printed_entry]['text']))
    print('Created on: {}'.format(str(data[printed_entry]['date'])))
    print()

def entry_update(data):
    entry_index = entry_list(data)
    selected_entry = input('Which entry would you like to view: ')
    printed_entry = entry_index[int(selected_entry) - 1]
    print('Entry {} contains the following text: '.format(printed_entry))
    print(str(data[printed_entry]['text']))
    updated_entry = input('Enter updated text: ')
    data[printed_entry]['text'] = updated_entry
    data[printed_entry]['updated'] = datetime.datetime.now()
    print('Updated text: {}'.format(str(data[printed_entry]['text'])))

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
