# Ask user for an integer between 1 and 200.
def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def factor(var_to_factor):

    factors_list = []

    # square root the number to work out when to stop looping.
    stop = var_to_factor ** 0.5
    stop = int(stop)

    for item in range(1, stop + 1):

        # check to see if the item is a factor
        if to_factor % item == 0:
            factors_list.append(item)

            # Calculate partner
            partner = to_factor // item

            # Add partner to the list (but prevent duplicate entries)
            if partner != item:
                factors_list.append(partner)

    return factors_list


# Main Routine Goes Here
while True:

    # Ask user for number to factor
    to_factor = num_check("To factor: ")

    # Check to see if the exit code has been entered
    if to_factor == "xxx":
        break

    # factorise the number
    all_factors = factor(to_factor)
    print(all_factors)

print("\nThanks for using the this tool")
