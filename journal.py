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

    # journal data, empty array until we get json added.

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
            #write_journal(journal_data,journal_file)
        elif menu_entry == 'p':
            # print the text of the entry
            entry_print(journal_data)
        elif menu_entry == 'u':
            # update text of entry
            entry_update(journal_data)
            #write_journal( journal_data, journal_file)
        elif menu_entry != 'x':
            print('Sorry but {} is not a choice at this time please choose again'.format(menu_entry))

    write_journal( journal_data, journal_file )



def entry_add(data):
    entry_title = input('Enter title for your entry: ')
    entry_text = input('Enter {} data: '.format(entry_title))
    entry_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data.append ( {
        'title': entry_title,
        'content': entry_text,
        'date': entry_date
    })

    return data

def entry_list(data):

    if not data:
        print('Journal is empty')
        return

    for idx,entry in enumerate(data):
        print(str(idx +1) + ": " + str(entry['title']))


def entry_remove(data):
    entry_list(data)
    remove_item = int(input('Which item number would you like to remove: '))
    try:
        del data[remove_item -1]
    except KeyError:
        print('Journal removal error, index {} not present'.format(remove_item))
    return data

def entry_print(data):
    if len(data) == 0:
        print('Journal is empty')
        return
    entry_list(data)
    selected_entry = int(input('Which entry would you like to view: '))
    index_target = selected_entry -1
    print()
    print('Entry {} contains the following text: '.format(data[index_target]['title']))
    print(str(data[index_target]['content']))
    print('Created on: {}'.format(str(data[index_target]['date'])))
    print()

def entry_update(data):
    entry_list(data)
    selected_entry = int(input('Which entry would you like to view: '))
    index_target = selected_entry -1
    print('Entry {} contains the following text: '.format(data[index_target]['title']))
    print(str(data[index_target]['content']))
    updated_entry = input('Enter updated text: ')
    data[index_target]['content'] = updated_entry
    data[index_target]['updated'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('Updated text: {}'.format(str(data[index_target]['content'])))

def open_journal(jfile):
    # open the file, create if not present
    data = []

    try:
        with open(jfile, 'r+') as input:
            data = json.load(input)
    except OSError:
        print('Unable to open file {}'.format(jfile))

    return data

def write_journal(data,jfile):
    #print(json.dumps(data, sort_keys=True, indent=4, default=str ))
    try:
        with open(jfile, 'w') as outfile:
           json.dump(data, outfile, sort_keys=True, indent=4, default=str )
    except OSError:
        print('Unable to open file {}'.format(jfile))


if __name__ == '__main__':
    main()
