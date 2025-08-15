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


def image_calc():
    pass
    width = int_check("width: ", 1)
    height = int_check("height: ", 1)

    num_pixels = width * height
    num_bits = num_pixels * 24



    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer

images_ans = image_calc()
print(images_ans)

