def get_normalized_print(message):
    user_name = input(message)
    normalized_user_input = user_name.strip().title()
    print('Welcome,', normalized_user_input)

get_normalized_print("Enter your name: ")


def calculate_square_print(side_1, side_2):
    square = side_1 * side_2
    return square

square = calculate_square_print(4, 9)

print('Square =', square)
