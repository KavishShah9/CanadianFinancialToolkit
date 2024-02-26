import time


def seperator():
    """Prints a separator line to enhance readability."""
    print("-" * 110)


def general_info():
    """ The function prints the general information about the TFSA account"""
    seperator()
    print("\t\t\t\t\t\tTFSA: Tax Free Savings Account")
    seperator()
    print("TFSA is not a savings account; it is an INVESTMENT account. "
          "\nYou will only be able to take maximum advantage of TFSA if you have made profitable investments."
          "\n\nTFSA allows you to earn the interest 'TAX-FREE' unlike the regular taxable savings account.")
    seperator()


# Dictionary containing the status in Canada
status = {
    1: "Canadian Citizen",
    2: "Permanent Resident",
    3: "Temporary Resident (international student, foreign worker)",
    4: "Refugee or Protected Person",
    5: "Visitor (on visitors visa)"
}

# Dictionary stating the year and its corresponding contribution limit added by Canadian Government
contribution = {
    2009: 5000, 2010: 5000, 2011: 5000, 2012: 5000,
    2013: 5500, 2014: 5500, 2015: 10000, 2016: 5500,
    2017: 5500, 2018: 5500, 2019: 6000, 2020: 6000,
    2021: 6000, 2022: 6000, 2023: 6500, 2024: 7000,
}


def delay():
    """ The function will delay the printing on console to grab the attention of user """
    for x in range(3):
        time.sleep(0.75)
        print(".", end="")


total_contr_limit = 0


def printing_dict():
    """
    The function aims to print the year, its respective contribution and the gross total of TFSA
    depending on individual's status in Canada.
    """
    global total_contr_limit, contribution
    seperator()
    print("\nFetching your TFSA contribution data", end=" ")
    delay()
    print("\n")
    print("Year, Contribution")
    for keys, values in contribution.items():
        print("{0}:  $ {1:,}".format(keys, values))
    values = contribution.values()
    for val in list(values):
        total_contr_limit += val

    print("\nYour maximum/total contribution limit is: $ {0:,}".format(total_contr_limit))
    print("You can enjoy the TAX FREE dividend/interest gains by investing $ {0:,} in your TFSA account"
          .format(total_contr_limit))

    # Resetting the variables
    contribution.clear()
    contribution = {
        2009: 5000, 2010: 5000, 2011: 5000, 2012: 5000,
        2013: 5500, 2014: 5500, 2015: 10000, 2016: 5500,
        2017: 5500, 2018: 5500, 2019: 6000, 2020: 6000,
        2021: 6000, 2022: 6000, 2023: 6500, 2024: 7000,
    }
    total_contr_limit = 0
    seperator()


def tfsa_func():
    general_info()
    print("Choose from the following to check your eligibility status for TFSA:\n")

    for key, value in status.items():
        print("{0} : {1}".format(key, value))

    seperator()

    while True:
        try:
            status_input = int(
                input("\nEnter the number that associates with your living condition in Canada (between 1 and 5): "))
            if 1 <= status_input <= 5:
                # Valid input, proceed with the program logic
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    year_landed = 0
    age = 0

    if status_input == 1:

        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("\nFollow instructions properly. See ya next time.")

        if age < 18:
            print()
            seperator()
            print("Come back when you are 18 or above to open the TFSA account.")
            seperator()

        elif 18 <= age <= 120:
            for year in range((2024 + (17 - age)), 2008, -1):
                contribution.pop(year)
            printing_dict()
        else:
            print("\n\n")
            seperator()
            print("Kindly enter a valid age next time. See ya!")
            seperator()

    elif status_input == 2 or status_input == 3 or status_input == 4:
        try:
            year_landed = int(input("Enter the year in which you landed in Canada: "))
        except ValueError:
            print("\nFollow instructions properly. See ya next time.")

        if 2009 <= year_landed <= 2024:
            for year in range(year_landed - 1, 2008, -1):
                contribution.pop(year)
            printing_dict()
        elif 1900 < year_landed < 2009:
            printing_dict()
        else:
            print()
            seperator()
            print("Do not try to be over smart! Enter appropriate year")
            seperator()

    else:
        print()
        seperator()
        print("Sorry, you are not eligible for opening TFSA account in Canada on Visitors Visa")
        seperator()
