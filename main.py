import time
from TFSA import tfsa_func
from Taxes import taxes_func
from Millionaire import millionaire_func
from FHSA import is_eligible_for_fhsa, calculate_fhsa_investment

if __name__ == "__main__":

    def seperator():
        """Prints a separator line to enhance readability."""
        print("-" * 110)


    seperator()
    # General information about the project
    print("\t\t\t\t\t\t\t\tCanadian Financial Toolkit")
    print("This project aims to inform users about how money/taxes works in Canada through Canadian banking accounts.")
    print("It provides information on Tax-Free Savings Accounts (TFSA), First Home Savings Accounts (FHSA),")
    print("Registered Retirement Savings Plan (RRSP), calculating taxes for the year 2023, \n"
          "and estimating the time required to earn a specific amount of money.")
    seperator()

    # A list of options for the users to choose from.
    options = {
        1: "Check your Tax Free Savings Account (TFSA) status",
        2: "Calculate the tax you will pay for 2023",
        3: "Calculate how many years it will take for you to earn a millionaire/any amount",
        4: "Know about First Home Saving Account (FHSA) account and the amount of tax you will save by investing in it",
        5: "To exit the program"
    }

    while True:
        print("\n\n\n")
        for x in range(3):
            print("...", end=" ")
            time.sleep(0.6)
        print()
        seperator()
        # Displays the options menu
        for key, value in options.items():
            print("{} - {}".format(key, value))
        seperator()

        try:
            # Prompt user for choice
            user_choice = int(input("\nPlease select an option from the above list: "))

            if user_choice == 5:
                print()
                seperator()
                print("Bye Bye. See you next time!")
                seperator()
                break  # Exit the loop if the user chooses to exit

            elif user_choice in options:

                # Perform action based on user's choice
                if user_choice == 1:
                    print()
                    tfsa_func()  # Call function to check TFSA status
                elif user_choice == 2:
                    print()
                    taxes_func()  # Call function to calculate taxes for 2023
                elif user_choice == 3:
                    print()
                    millionaire_func()  # Call function to calculate time to become a millionaire
                elif user_choice == 4:
                    print()
                    eligible = is_eligible_for_fhsa()
                    calculate_fhsa_investment(eligible)
                else:
                    print("Nothing")

            else:
                print("Invalid option. Please select a valid number.\n")
        except ValueError:
            print("Invalid input. Please enter a number.")
