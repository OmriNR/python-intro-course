# Credit card validation

credit_card_number = input('Please enter your credit card number: ')

#Check length
valid_length = len(credit_card_number) == 16
print('Card is 16 digits long: ', valid_length);

valid_only_digits = credit_card_number.isnumeric()
print('Card contains digits only: ', valid_only_digits)

#Starts with 4 or 5
valid_start = credit_card_number[0] == '4' or credit_card_number[0] == '5'
print('Card starts with 4 or 5: ', valid_start)

#Last two digits are identical
valid_end = credit_card_number[-1] == credit_card_number[-2]
print('Last two digits are identical: ', valid_end)

if (valid_end and valid_length and valid_only_digits and valid_start):
    if (credit_card_number[0] == '4'):
        print('Card type: Visa')
    else:
        print('Card type: Mastercard')
    
    print(credit_card_number[:4]+'-****-****-'+credit_card_number[12:16])
else:
    print('Card is invalid')