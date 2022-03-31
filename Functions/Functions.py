# Rewrite your pay computation with 1.5x for overtime and create a function called computepay which takes two parameters (Hours and rate)

print("Alrighty then, let's get to work.")         


Valid = False                                   # Computepay takes the variables 'Hours' and 'PPHour' and converts them to 'Hour' and 'Rate' which it uses in its own local cycle
def computepay(Hour, Rate):                     # A set of code that can be called more than once without giant copy paste strips
    Hour = float(Hour)                          # Converts both variables to floats
    Rate = float(Rate)

    if Hour >= 40:                                                                                                                  # Checks if Hours worked is above 40
        pay = (Rate*1.5)                                                                                                        # Takes pay per hour and multiplies it by 1.5
        Compensation = ('Gross pay: ${}').format(pay)                                                                               # Formats the variable 'pay' into the string
        print('Congratulations! The company deems you worthy of further compensation, your pay has been raised by 1.5 times!')              # Flavour text
        print(Compensation)                                                                                                             # Prints resultant compensation

    elif Hour < 40:                                                                                                        # Checks if hours worked is under 40
        print('Unfortunately our company deems you incapable of further compensation, try harder next time!')               # If hours worked is not above 40 then a discouraging message appears
        NoCompensate = ('Gross pay: ${}').format(Rate)                                                                    # Formats the variable 'NoCompensate' 
        print(NoCompensate)                                                                                                      # Prints original value of 'PPHour' in a string

                                                            
while Valid is False:                                                   # Loops program as long as Valid is False

    Hours = input('Hours Worked: ')                                     # Takes input from user
    PPHour = input('Money Per Hour: ')

    try:                                                                         
        computepay(Hours, PPHour)                                           # Calling the function for the if else statement above
        Valid = True                                                        # Setting the state doesnt break the loop if its in the defined function

    except:                                                                         
        print('The character(s) you inputted was invalid, please try again')
        Valid = False                                                               # Sets valid to False so the program try function repeats
        
                                                                       
input('-Press Any Key to Exit Program-')                # Prevents program from closing until key is pressed


