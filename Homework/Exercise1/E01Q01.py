# Calculte the bill + tip

bill = int(input('Please enter the bill amount: '));
tip_percent = int(input('Please enter the tip percentage: '));

if (tip_percent > 100 or tip_percent <= 0):
    print('Tip percentage is invalid, Please enter tip between 0 and 100');
else:
    tip = bill * (tip_percent / 100)
    print('Tip amount: ', tip)

    total = bill + tip
    print('Total to pay: ', total)