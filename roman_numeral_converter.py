import sys

arabic_numerals = [1000, 500, 100, 50, 10, 5, 1]
roman_numerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

#checks that  initial input is valid then returns if input is 'roman' or 'arabic'
def initial_input_checker():
    if the_input.isalnum():
        if the_input.isalpha():
            for letter in the_input:
                if letter.upper() not in roman_numerals:
                    print("Invalid input - Roman numerals consist of: "
                    + "I, V, L, C, D, M ")
                    sys.exit()
            return "roman_choice"
        elif the_input.isnumeric():
            if the_input[0] == '0':
                print("The number cannot start with a zero please try again")
                sys.exit()
            elif int(the_input) < 0 or int(the_input) > 3999:
                print("That's not a number between 1 and 3999 please try again")
                sys.exit()
            else:
                return "arabic_choice"
        else:
            print("Incorrect format, please try again")
            sys.exit()
    else:
        print("Incorrect format, please try again")
        sys.exit()

## Arabic to Roman Processing
#converts digits into: thousands, hundreds, tens and digits
def arabic_to_roman_value_split():
    number_length = 1
    value_split = []
    for i in range(len(the_input) - 1):
        number_length *= 10
    for i in range(len(the_input)):
        value = int(the_input[i]) * number_length
        if value != 0:
            value_split.append(value)
            number_length = number_length // 10
        elif value == 0:
            number_length = number_length // 10
    return value_split

#creating a list if the converted values match roman numerals, including rules
def arabic_to_roman():
    value_list = []
    for value in arabic_to_roman_value_split():
        for i in range(len(arabic_numerals)):
            if value == arabic_numerals[i]:
                value_list.append(roman_numerals[i]); break
            elif (arabic_numerals[i] * 2) == value:
                value_list.append((roman_numerals[i]) * 2); break
            elif (arabic_numerals[i] * 3) == value:
                value_list.append((roman_numerals[i]) * 3); break
            elif (arabic_numerals[i] * 4) == value:
                value_list.append(roman_numerals[i])
                value_list.append(roman_numerals[i - 1]); break
            elif (arabic_numerals[i] * 6) == value:
                value_list.append(roman_numerals[i - 1])
                value_list.append(roman_numerals[i]); break
            elif (arabic_numerals[i] * 7) == value:
                value_list.append(roman_numerals[i - 1])
                value_list.append((roman_numerals[i]) * 2); break
            elif (arabic_numerals[i] * 8) == value:
                value_list.append(roman_numerals[i - 1])
                value_list.append((roman_numerals[i]) * 3); break
            elif (arabic_numerals[i] * 9) == value:
                value_list.append(roman_numerals[i])
                value_list.append(roman_numerals[i - 2]); break
    final_result = ''
    print(f"\nThe result of converting {the_input} into Roman Numerals is: "
    + f"{final_result.join(value_list)}\n")

## Roman to Arabic Processing
#creates a list of each letter of roman numeral input
def roman_to_arabic_preliminary():
    list_of_roman_input = list(the_input)
    numeral_list = []
    for roman_numeral in list_of_roman_input:
        for i in range(len(roman_numerals)):
            if roman_numeral.upper() == roman_numerals[i]:
                numeral_list.append(arabic_numerals[i])
    return numeral_list


def roman_to_arabic():
    prelim_numerals = roman_to_arabic_preliminary()
    final_numeral_list = []
    for idx in range(0, len(prelim_numerals) - 1):
        if prelim_numerals[idx] != 0:
            if prelim_numerals[idx + 1] > prelim_numerals[idx]:
                final_numeral_list.append(prelim_numerals[idx + 1] - prelim_numerals[idx])
                prelim_numerals[idx + 1] = 0
            else:
                final_numeral_list.append(prelim_numerals[idx])
    final_result = sum(final_numeral_list) + prelim_numerals[-1]
    print(f"\nThe result of converting '{the_input.upper()}' "
    + f"into Arabic Numerals is: {final_result}\n")


#Program Execution
print("\nThis calculator converts between Roman Numerals and Arabic Numerals\n")
the_input = input("Enter a number in either Roman Numerals or Arabic Numerals:\n")
initial_input_checker()
if initial_input_checker() == 'arabic_choice':
    arabic_to_roman_value_split()
    arabic_to_roman()
elif initial_input_checker() == 'roman_choice':
    roman_to_arabic_preliminary()
    roman_to_arabic()