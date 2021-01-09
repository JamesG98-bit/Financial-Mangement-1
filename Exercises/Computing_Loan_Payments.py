def month_pay(rate, years, amount):

    a = amount * rate
    b = 1 - (1 / ((1 + rate) ** (years * 12)))

    return print("£ {:.2f}".format(a // b))


if __name__ == '__main__':

    while True:
        try:
            RATE = float(input('Please enter the monthly interest rate as a decimal... '))
            break
        except ValueError:
            print('Incorrect, try entering a whole value such as 0.10.')

    while True:
        try:
            YEARS = int(input('Please enter the number of years as a whole integer... '))
            break
        except ValueError:
            print('Incorrect, try entering a whole value such as 2.')

    while True:
        try:
            AMOUNT = float(input('Please enter the amount... '))
            break
        except ValueError:
            print('Incorrect, try entering a numerical value such as 10000.')

    month_pay(RATE, YEARS, AMOUNT)
