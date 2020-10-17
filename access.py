storage = {}


def usernameChecker(username):
    alpha = ('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m')
    for i in alpha:
        i = i.upper()
        if i in username:
            return True
    else:
        return 'true'


def passwordChecker(password):
    alpha = ('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m')
    numbers = (1,2,3,4,5,6,7,8,9,0)
    characters = ("!","@",'#','$','%','^','&','*','(',')','-','_','+','=',',',':','/','>','<','?','.'," \ ", "|", '£', '~', ';')
    if len(password) >= 8:
        for i in alpha:
            i = i.upper()
        for number in numbers:
            number = str(number)
        for character in characters:
            if alpha and number and character in password:
                return True
    else:
        return 'true'


while True:
    prompt = input('Enter Your option here: ').lower()
    prompt = prompt.strip()
    # to sign up
    if prompt == 'sign up':
        username = input('Enter username: ')
        x = usernameChecker(username)
        password = input('Enter password: ')
        y = passwordChecker(password)
        if x == True and y == True:
            for key in storage:
                # print(key)
                # check if username exists
                if username in key:
                    print('Username Exist')
                    break
            # if all requirements fine, map password to its username
            else:
                storage[username] = password
                print('Information saved!')
        # if one or more requirements failed;
        else:
            if x == 'true' and y == True:
                print('Username doesn\'t meet the requirement.')
            elif x == True and y == 'true':
                print('Password doesn\'t meet up with the requirements.')
            elif x == 'true' and y == 'true':
                print('Username and Password didn\'t meet up with the requirements.')
            # print(storage)

        restart = input('Enter y to continue or n to quit(y/n): ').lower()
        restart = restart.strip()
        if restart == 'y':
            continue
        elif restart == 'n':
            quit()
        else:
            print('I do not understand')
    
    # for logging in         
    elif prompt == 'login':
        username = input('Enter username: ')
        password = input('Enter password: ')
        # check if username and password exists
        for key, value in storage.items():
            if username in key and password in value: 
                print("Access Granted")
                quit()
        # if username or password doesn't exist
        else:
            if username in key and storage[username] != password:
                print('Password Incorrect')
            elif username not in key and password in value:
                print('Username Incorrect')
            elif username not in key and password not in value:
                print('Invalid Login detais')

    # if change password if forgotten
    elif prompt == 'forgotten':
        username = input('Enter Username: ')
        # check if username exist, if yes, map a new password to it 
        for key in storage:
            if username in key:
                password = input('Enter new password: ')
                y = passwordChecker(password)
                if y == True:
                    storage[username] = password
                    # print(storage)
                    break
                else:
                    print('Password doesn\'t meet the requirements.')
        # if username not found
        else:
            print('Username not found.')
            
    # if user input unknown
    else:
        print('''
Enter 'sign up' to open a new account
Enter 'login' to access dashboard
Enter 'forgotten' if password can't be remembered
''')