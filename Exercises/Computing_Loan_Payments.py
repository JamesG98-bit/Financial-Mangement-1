def month_pay(RATE, YEARS, AMOUNT):

    A = AMOUNT * RATE
    B = 1 - (1/(1+(RATE/12) * (YEARS * 12)))

    return A / B

if __name__ == '__main__':
    input()