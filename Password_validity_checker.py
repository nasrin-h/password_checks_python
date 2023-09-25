#Password_validity_checker

import re
import sys

def check_upper(pwd):
	return bool(re.search(r'[A-Z]', pwd))

def check_lower(pwd):
	return bool(re.search(r'[a-z]', pwd))

def check_number(pwd):
	return bool(re.search(r'[0-9]', pwd))

def check_special(pwd):
	return bool(re.search(r'[!@£$%^&?]', pwd))

def check_blanks(pwd):
	return bool(re.search(r'\s',pwd))

def check_length(pwd):
	return 8<=len(pwd)<=15

pwd = input('Please enter your password: ')

if all([check_upper(pwd), 
	    check_lower(pwd),
	    check_number(pwd),
	    check_special(pwd),
	    not check_blanks(pwd),
	    check_length(pwd)]):
    print('Your password has met all requirements')
else:
 	print('Your password has not met the following requirement(s): ')

 	if not check_upper(pwd):
 		print(' Password must have at least one upper case character')
 	if not check_lower(pwd):
 		print(' Password must have at least one lower case character')
 	if not check_number(pwd):
 		print(' Password must have at least one number')
 	if not check_special(pwd):
 		print(' Password must have at least one special character')
 	if check_blanks(pwd):
 		print(' Password must not have any spaces')
 	if not check_length(pwd):
 		print(' Password must be between 8 to 15 characters long')
