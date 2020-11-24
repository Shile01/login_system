import re as regex
storage = {}


def usernameChecker(username):
    # contains uppercase
    pattern = regex.compile('^[A-Z]*$')
    if regex.search(pattern, username):
        return True
    else:
        return False


def passwordChecker(password):
    # contains uppercase
    # contains lowercase
    # contains numeric
    # contains special character
    pattern = regex.compile('[A-Za-z0-9@#$%^&+=]{8,}')
    if regex.search(pattern, password):
      return True
    else:
      return False
    
def signUp ():
    username = input('Enter username: ')
    validUsername = usernameChecker(username)
    password = input('Enter password: ')
    validPassword = passwordChecker(password)
    # what can go wrong?
    # username exist?
    if username in storage:
        print('Username Exist')
        return False
    # bad username?
    elif validUsername == False and validPassword:
        print('Username doesn\'t meet the requirements.')
        return False
    # bad password?
    elif validUsername and validPassword == False:
        print('Password doesn\'t meet the requirements.')
        return False
    # bad username & password
    elif validUsername == False and validPassword == False:
        print('Password and Username doesn\'t meet the requirements.')
        return False
    # all good sign up
    else:
        storage[username] = password
        print('Information saved!')
        return True

def signIn ():
    username = input('Enter username: ')
    password = input('Enter password: ')
    # what can go wrong?
    # bad username?
    if username not in storage:
        print('Username Incorrect')
        return False
    # bad password?
    elif storage[username] != password:
        print('Password Incorrect')
        return False
    # both ok?
    elif username in storage and storage[username] == password:
        print('Access Granted')
        return True
    # both invalid?
    else:
        print('Invalid details')
        return False
        
def changePassword ():
    username = input('Enter username: ')
    validUsername = usernameChecker(username)
    # what can go wrong?
    # bad username?
    if validUsername == False:
        print('Username doesn\'t meet the requirements.')
        return False
    # registered?
    elif username in storage:
        print('User Found!')
        password = input('Enter new password: ')
        validPassword = passwordChecker(password) 
        if validPassword == True:
            storage[username] = password
            print("New password for " + username + " is " + password)
            return True
        else:
            print('Password doesn\'t meet the requirements.')
            return False
        
def __init__ ():
  print(
    "HINT::: \n" +
    "Enter 'sign up' to open a new account \n" +
    "Enter 'login' to access dashboard \n" +
    "Enter 'forgotten' if password can't be remembered \n"
  )
  action = input("\nEnter startup action: ")
  if action == "sign up":
    signingUp = signUp()
    if signingUp:
      print("\nSign up successful\n")
      __init__()
    else:
      print("\nSign up came back with one or more error(s)\n")
      restart = input("\nDo you want to try again? ")
      if "yes" in restart or "y" in restart:
        __init__()
      else:
        print("Thanks for using this program\nSee you some other time")
        quit()
  if action == "login":
    signingIn = signIn()
    if signingIn:
      print("\nSign in successful\n")
      __init__()
    else:
      print("\nSign in came back with one or more error(s)\n")
      restart = input("\nDo you want to try again? ")
      if "yes" in restart or "y" in restart:
        __init__()
      else:
        print("Thanks for using this program\nSee you some other time")
        quit()
  if action == "forgotten":
    changingPassword = changePassword()
    if changingPassword:
      print("\nPassword Changed successfully\n")
      __init__()
    else:
      print("\nOne or more error(s) prevented password change\n")
      restart = input("\nDo you want to try again? ")
      if "yes" in restart or "y" in restart:
        __init__()
      else:
        print("Thanks for using this program\nSee you some other time")
        quit()

__init__()
