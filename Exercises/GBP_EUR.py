import quandl

if __name__ == '__main__':

    while True:
        try:
            amount = float(input('Please enter the amount to convert... '))
            break

        except ValueError:
            print('You must enter a numerical value.')

    rate = quandl.get("ECB/EURGBP")

    exchange = rate.iloc[-1]['Value']

    print(f'£{amount:.2f} converted to €{amount ** exchange:.2f}')

