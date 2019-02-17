import datetime

def main():
    banner()
    run_event_loop()


def banner():
    print('-----------------------------------')
    print('---       My Journal Practice   ---')
    print('-----------------------------------')

def menu():
    user_choice = input("Would you like to [A]dd, [L]ist journal entries or E[x]it: ").lower().strip()
    return user_choice

def run_event_loop():

    # set to False for init value of loop
    menu_entry = False

    # journal data, empty dict until we get json added.
    journal_data = {}

    while menu_entry != 'x':
        menu_entry = menu()

        if menu_entry == 'a':
            # Add a item
            journal_data = entry_add(journal_data)
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


if __name__ == '__main__':
    main()
