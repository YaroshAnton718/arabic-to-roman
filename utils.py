def arabic_to_roman(num):
    """
    Converts from arabic to roman and returns in string format.

    Parameters:
        num (int): an arabic number to convert

    Returns:
        string: the roman numeral as a string
    """
    result = []
    num, arr = roman(num, 1000, 'M')
    result += arr
    num, arr = roman(num, 900, 'CM')
    result += arr
    num, arr = roman(num, 500, 'D')
    result += arr
    num, arr = roman(num, 400, 'CD')
    result += arr
    num, arr = roman(num, 100, 'C')
    result += arr
    num, arr = roman(num, 90, 'XC')
    result += arr
    num, arr = roman(num, 50, 'L')
    result += arr
    num, arr = roman(num, 40, 'XL')
    result += arr
    num, arr = roman(num, 10, 'X')
    result += arr
    num, arr = roman(num, 9, 'IX')
    result += arr
    num, arr = roman(num, 5, 'V')
    result += arr
    num, arr = roman(num, 4, 'IV')
    result += arr
    num, arr = roman(num, 1, 'I')
    result += arr

    return ''.join(result)

def roman(i, j, c):
    """
    Processes the number from 'M' to 'I'.

    Parameters:
        i (int): an arabic number
        j (int): main numbers from roman in arabic
        c (string): a roman symbol that appends to result array

    Returns:
        i (int): an arabic number after processing
        arr (list): an array of result
    """
    arr = []
    while i >= j:
        arr.append(c)
        i -= j

    return i, arr

def get_number():
    """
    Receives the number from user and validates it.

    Returns:
        number (int): received number from user
    """
    while True:
        print("This program translates from arabic number to roman number.")
        try:
            number = int(input("Enter the number [1-3999]: "))
        except ValueError:
            print("Please enter a number.\n")
            continue

        if number < 1 or number > 3999:
            print("Please, enter a number in diapason.\n")
            continue

        return number

def choice():
    """
    Gives user a choice: continue or not.
    """
    while True:
        num = get_number()
        print(f"Result: {arabic_to_roman(num)}")

        while True:
            choice = input("\nWould you like to continue? (y/n): ")
            if choice == "y" or choice == "Y":
                break
            elif choice == "n" or choice == "N":
                exit(0)
            else:
                print("Please enter y or n.\n")
                continue

