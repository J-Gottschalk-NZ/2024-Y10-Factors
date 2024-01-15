# Functions go here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    
    # Make string with five characters 
    ends = decoration * 5
    
    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)
    
    print()
    print(statement)
    print()
    
    return ""
    

# displays instructions / information
def instructions():
    
    statement_generator("Instructions /  Information", "=")
    print()
    print("Please enter an integer that is one or more.  The program will output a list of the numbers factors.")
    print("The program will also tell you if... ")
        
    print("- the number is a prime number (has only two factors) ")
    print(" - is a perfect square")
    print()
    print("Press <enter> to find the factors of another number or any key to quit")
          
    print()
    return ""     


# checks input is a number more than a given value
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter an integer between 1 and 200 (inclusive)"
        
        try:
        
            # ask user to enter a number
            response = int(input(question))
            
            # checks number is between 1 and 200
            if 1 <= response <= 200:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    

# gets factors, returns a sorted list
def get_factors(to_factor):
    
    # list to hold factors
    factors = []
        
    # Square root to_factor to find 'half way'
    limit = int(to_factor ** 0.5)
    
    # find factor pairs and add to list
    for item in range (1, limit + 1):
        
        # check factor is not 1 (unity)
        if to_factor == 1:
            break
        
        # check if number is a factor
        result = to_factor % item
        factor_1 = to_factor // item
               
        # add factor to list if it is not already in there
        if result == 0:
            
            # add item to list
            factors.append(item)
            
        if factor_1 != item and result == 0:
            factors.append(factor_1)
            
        # sort list...
    
    factors.sort()
        
    return factors



# Main Routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":
    
    comment = ""
    
    # ask user for number to be factored...    
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:            
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY!  It only has one factor.  Itself :)"
        
    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)
        
    # output factors and comment
    
    # Generate heading...    
    if var_to_factor == 1:
        heading = "One is special..."
        
    else:
        heading = "Factors of {}".format(var_to_factor)
    
    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()