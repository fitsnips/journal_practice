

def main():
    banner()
    run_event_loop()


def banner():
    print('-----------------------------------')
    print('---       My Journal Practice   ---')
    print('-----------------------------------')

def menu():
    user_choice = input("Would you like to [A]dd journal entry or E[x]it: ").lower().strip()
    return user_choice

def run_event_loop():

    # set to False for init value of loop
    menu_entry = False

    while menu_entry != 'x':
        menu_entry = menu()

        if menu_entry == 'a':
            # Add a item
            print('Adding a item')
        elif menu_entry != 'x':
            print('Sorry but {} is not a choice at this time please choose again'.format(menu_entry))


if __name__ == '__main__':
    main()
