import re

def check_digit(pwd: str) -> bool:
    return bool(re.search(r'[0-9]', pwd))

def check_uppercase(pwd: str) -> bool:
    return bool(re.search(r'[A-Z]', pwd))

def check_lowercase(pwd: str) -> bool:
    return bool(re.search(r'[a-z]', pwd))

def check_speacial_char(pwd: str) -> bool:
    return bool(re.search(r'[~!@#$%^&*?]', pwd))

def check_white_space(pwd: str) -> bool:
    return bool(re.search(r'\s', pwd))

def check_length(pwd: str) -> bool:
    return 6<=len(pwd)<=12

pwd = input('Check your password strength: ')

if all([check_digit(pwd),
        check_lowercase(pwd),
        check_uppercase(pwd),
        check_speacial_char(pwd),
        not check_white_space(pwd),
        check_length(pwd)]):
    print(' Your password is strong, you are good to go!')
else:
    print(' Your password has not met the following requirements(s):')

    if not check_digit(pwd):
        print(' - Password must have at least one digit (0-9)')

    if not check_uppercase(pwd):
        print(' - Password must have at least one upper-case letter (A-Z)')
    
    if not check_lowercase(pwd):
        print(' - Password must have at least one lower-case letter (a-z)')

    if not check_speacial_char(pwd):
        print(' - Password must have at least one special characters (~!@#$%^&*?)')

    if check_white_space(pwd):
        print(' - Password must NOT contain white space characters')

    if not check_length(pwd):
        print(' - Password length must be at least 6 character and at most 12 characters')

