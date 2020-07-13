

def main():

        print('Hello and welcome to my simple calculator.')
        print('This is will display different numerical data as a test.')

        value = float(input("Please enter a number: "))
        value2 = float(input("Please enter a second number: "))

        print('These are your two numbers added together: ', (float(value)) + (float(value2)))
        print('These are your two numbers subtracted: ', (float(value) - (float(value2))))
        print('These are your two numbers multiplied: ', (float(value) * (float(value2))))
        print('These are your two numbers divided: ', (float(value)) / (float(value2)))


        restart = input("Do you want to restart? [y/n] >")
        if restart== 'y':
            main()
        else:
            print('Thank you, Goodbye.')
            exit



main()


