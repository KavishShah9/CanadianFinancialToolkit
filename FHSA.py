from TFSA import delay
from Taxes import Person, province_list, provincial_taxes


def seperator():
    """Prints a separator line to enhance readability."""
    print("-" * 110)


def is_eligible_for_fhsa():

    # First Home Savings Account (FHSA) general information
    seperator()
    print("What is an FHSA?")
    print("The First Home Savings Account (FHSA) is a registered account introduced by Canadian government in 2022\n"
          "To help first-time homebuyers save for their down payment tax-free.")

    seperator()
    print("Eligibility:")
    print("* You must be 18 years of age or older (the age of majority in your province).")
    print("* You must have a valid Social Insurance Number (SIN).")
    print("* You cannot have owned a home in the past four years.")

    seperator()
    print("Contribution Limits:")
    print("* You can contribute up to $8,000 per year to your FHSA, with a lifetime limit of $40,000.")
    print("* Contributions are tax-deductible, meaning they reduce your taxable income for the year.")

    seperator()
    print("Withdrawals")
    print("* Withdrawals used to purchase a qualifying first home are tax-free.")
    print("* Unused funds can be transferred to an RRSP or RRIF without affecting your contribution room.")
    print("* Non-qualifying withdrawals are taxed as income and may be subject to an additional 1% penalty.")

    seperator()
    print("Additional Information:")
    print("* You can open an FHSA at most financial institutions in Canada.")
    print("* The FHSA complements, not replaces, other home ownership programs.")
    print("* For more information and eligibility requirements, visit the Canada Revenue Agency website:")

    print("\n**Disclaimer:**")
    print("This information is for general purposes only and does not constitute professional financial advice."
          "Please consult with a qualified financial advisor for personalized advice.")
    seperator()

    """Determines eligibility for opening an FHSA account based on user input.

    Returns:
        True if eligible, False otherwise.
    """

    # Ensure validity of age input
    seperator()
    print("We would like to ask you 3 questions to check your eligibility to open FHSA account")

    while True:
        try:
            age = int(input("\n1) How old are you?: "))
            if age < 18:
                break
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid age (integer number).")

    # Validate SIN number format
    while True:
        sin_number = input("2) Do you have a valid SIN number (Y/N)? ").upper()
        if sin_number not in ("Y", "N"):
            print("\nInvalid input. Please answer 'Y' for yes or 'N' for no.")
        else:
            break

    # Case-insensitive conversion for qualifying ownership of home
    while True:
        has_qualifying_home = input(
            "3) Have you or your spouse/common-law partner owned a qualifying home in the past 4 years (Y/N)? ").upper()
        if has_qualifying_home not in ("Y", "N"):
            print("Invalid input. Please answer 'Y' for yes or 'N' for no.")
        else:
            break

    # Eligibility check based on age and SIN requirements
    if age >= 18 and sin_number == "Y" and has_qualifying_home == "N":
        return True
    else:
        return False


def calculate_fhsa_investment(eligible_or_not):

    """Calculates recommended annual FHSA investment based on eligibility.
    Args:
        eligible_or_not (bool): Whether the user is eligible for FHSA.
    Returns:
        None if not eligible, otherwise prints message with recommendation.
    """

    if not eligible_or_not:
        seperator()
        print("We are sorry, you are not eligible to open an FHSA account.\n")
        print("To be eligible to open FHSA account, you must be:")
        print("1) 18 or above")
        print("2) holding a valid SIN number")
        print("3) not have owned a qualifying home in the past 4 years")
        seperator()
        return

    seperator()
    print("Congrats, you are eligible to open FHSA account.")
    seperator()

    # Recommend maximum contribution (case-insensitive for user input)
    print("Maximum contribution limit per year to invest in FHSA account is $8,000")
    value_ranges = {
        1: 4000,
        2: 5000,
        3: 8000
    }
    for key, value in value_ranges.items():
        print("{} - $ {}".format(key, value))

    while True:
        index = input("\nPick number from 1, 2 or 3 that associates annual investment: ").upper()
        if index.isdigit() and index in ["1", "2", "3"]:  # Check if the input consists only of digits
            index = int(index)
            x = value_ranges[index]
            break  # Exit the loop if the input is successfully converted to an integer
        else:
            print("Invalid input. Please enter an integer.")

    seperator()
    print(f"Investment amount: ${value_ranges[index]} per year.\n")
    years = 1
    count = 0
    inv_per_year = value_ranges[index]
    while value_ranges[index] <= 40000:
        print("Year {0:2}, Cumulative Invested: {1:,.1f}".
              format(years, value_ranges[index], 40000 % value_ranges[index]))
        value_ranges[index] += inv_per_year
        years += 1
        count += 1

    seperator()
    print("\nNow, we will calculate how much taxes you would save "
          "while investing in FHSA account ... ...", end=" ")
    delay()
    print()

    province_list()

    province = input("\nFrom above list, enter exact spelling of your province of residence: ")

    while province not in provincial_taxes:
        print("\nKindly enter the exact spelling of Province. First letters should be capital")
        province = input("From above list, enter exact spelling of your province of residence: ")

    try:
        income = int(input("Enter your total annual income: "))
    except ValueError:
        print("Please enter a valid income next time.")
        exit()

    person1 = Person(province, income)
    fd_tax = person1.federal_tax_calc(print_=False)
    pv_tax = person1.provincial_tax_calc(print_=False)
    total_tax = pv_tax + fd_tax
    seperator()
    print("Tax paid WITHOUT FHSA investment for {0} years : $ {1:,.2f}".format(count, total_tax * count))

    if value_ranges[index] < person1.income:
        person1.income -= x
        fd_tax_2 = person1.federal_tax_calc(print_=False)
        pv_tax_2 = person1.provincial_tax_calc(print_=False)
        total_tax_2 = pv_tax_2 + fd_tax_2
        print("Tax paid WITH FHSA investment for {0} years    : $ {1:,.2f}".format(count, total_tax_2 * count))
        seperator()
        print("So, by investing $ {0:,.2f} for {1} years, you will save $ {2:,.2f} in taxes".
              format(value_ranges[index], count, (total_tax - total_tax_2) * count))
        seperator()
        print()
    else:
        print("Not possible to invest more than your income ... ...")
