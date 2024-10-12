alphabets = ['A',
             'B',
             'C',
             'D',
             'E',
             'F',
             'G',
             'H',
             'I',
             'J',
             'K',
             'L',
             'M',
             'N',
             'O',
             'P',
             'Q',
             'R',
             'S',
             'T',
             'U',
             'V',
             'W',
             'X',
             'Y',
             'Z',]
code_symbols = list(reversed(alphabets))
choices = {'1': "Generate a coded message",
           '2': "Decode a coded message",}
choice = None

while choice != "0":
    if choice == "1":
        message = input("Enter your message: \n")
        coded_message = ''

        for letter in message:
            coded_message += code_symbols[alphabets.index(letter)]

        print("Your coded message is: ")
        print(coded_message)
        break

    elif choice == "2":
        coded_message = input("Enter your coded message: \n")
        message = ''

        for letter in coded_message:
            message += alphabets[code_symbols.index(letter)]
        print("Your decoded message is: ")
        print(message)
        break

    else:
        for key, value in choices.items():
            print(f"{key}: {value}")
        print("0: Exit")

    choice = input(": ")
