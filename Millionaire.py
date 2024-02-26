import csv
import time


def seperator():
    """Prints a separator line to enhance readability."""
    print("-" * 110)


def delay():
    """ The function will delay the printing on console to grab the attention of user """
    for x in range(3):
        time.sleep(0.9)
        print(".", end="")


def millionaire_func():

    seperator()
    print("In order to calculate the number of years it will take you to become a millionaire/any amount, "
          "\nyou have to answer the following questions")
    seperator()

    # Constants
    initial_investment = 0
    interest_rate = 0.08
    inflation_rate = 0.0312
    extra_investment = 500
    current_year = 2024

    while True:
        try:
            annual_investment = int(input("\nEnter annual investment amount: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            goal = int(input("Enter the goal that you want to achieve. E.g: 1000000: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # annual_investment = int(input("Enter annual investment amount: "))
    ann_inv = annual_investment

    # Initialize variables
    fund = annual_investment
    serial_number = 1
    years = 0

    # Create and open CSV file for writing
    with open('investment_details.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([' Years', 'Year', 'Investment/year', 'Interest Earned', 'Fund', 'Inflation Adjusted Fund'])

        while fund < goal:
            interest_earned = fund * interest_rate
            fund += interest_earned

            # Adjust for inflation
            inflation_adjusted_fund = fund / (1 + inflation_rate) ** (current_year - 2023)

            writer.writerow([serial_number, current_year, '{:.2f}'.format(initial_investment + annual_investment),
                             '{:.2f}'.format(interest_earned), '{:.2f}'.format(fund),
                             '{:.2f}'.format(inflation_adjusted_fund)])

            if (current_year - 2024) % 5 == 0:
                annual_investment += extra_investment

            fund += annual_investment

            initial_investment = 0
            current_year += 1
            years += 1
            serial_number += 1

    seperator()
    print("It will take {} years to make $ {:,.2f} by investing {:,.2f} annually at {}%."
          .format(years, goal, ann_inv, interest_rate * 100), end=" ")

    # Read data from CSV file and print with proper formatting
    with open('investment_details.csv', mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    delay()
    print()
    seperator()
    # Print data with proper formatting and commas
    print('{:^8} {:^8} {:^16} {:^16} {:^16} {:^24}'.format(*data[0]))

    for row in data[1:]:
        formatted_row = [int(row[0]), int(row[1]), '{:,.2f}'.format(float(row[2])),
                         '{:,.2f}'.format(float(row[3])), '{:,.2f}'.format(float(row[4])),
                         '{:,.2f}'.format(float(row[5]))]
        print('{:^8} {:^8} {:^16} {:^16} {:^16} {:^24}'.format(*formatted_row))

    print("\nPS: After every 5 years, an extra $500 amount is added to the investment to compensate inflation")
    print("The above data is added in the CSV file for you!")
    seperator()
