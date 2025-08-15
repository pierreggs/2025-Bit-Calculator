def int_check(question, low):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

           # check th
            # at the number is more than zero
            if response >= low:
                return response
            else:
                print(error)


        except ValueError:
            print(error)


def integer_calc():

    integer = int_check("integer: ", 0)

    raw_binary = bin(integer)

    binary = raw_binary[2:]
    num_bits = len(binary)



    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."

    return answer

integer_ans = integer_calc()
print(integer_ans)

