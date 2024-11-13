#Program divides two numbers based on a user input

def main():
    while True:
        
        #Uses a try/except to display an error rather than a general Python error
        try:
            #Gets 2 inputs from a user
            int1 = int(input("Please enter a number: "))
            int2 = int(input("Please enter another number: "))

            while True:
                try:
                    #Divides input1 by input2
                    result = int1 / int2

                    #If valid, prints the result
                    print(f"The result is: {result}")
                    #Exit the function if division is successful
                    return

                #Error if result isn't valid
                except ZeroDivisionError:
                    print(f"Whoops, you cannot divide {int1} by {int2}. Please enter another number.")
                    int2 = int(input("Please enter another number: "))

        #Error if user does not enter an int
        except ValueError:
            print("Invalid input. Please enter valid integers.")

#Calls the main function
if __name__ == "__main__":
    main()