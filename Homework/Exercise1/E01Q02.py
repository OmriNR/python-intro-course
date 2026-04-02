# Username validation

username = input('Choose a username: ')

#Check username length
valid_length = len(username) >= 5 and len(username) <= 12
print('Your username is of proper length (5-12): ', valid_length);

#Check if username starts with letter
valid_start = not username[0].isdigit()
print('Your username starts with a letter: ', valid_start)

#Check if username ends with digit
valid_finish = username[-1].isdigit()
print('Your username ends with a digit: ', valid_finish)

#Check if username does not have spaces
valid_no_spaces = ' ' not in username
print('Your username contains no spaces: ', valid_no_spaces)

#Check if username does not contain admin or root
valid_no_forbidden = ('admin' not in username) and ('root' not in username)
print("Your username doesn't contain forbidden words: ", valid_no_forbidden)

print('Your username is valid: ', valid_no_forbidden and valid_finish and valid_length and valid_start and valid_no_spaces)