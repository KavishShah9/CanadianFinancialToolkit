import webbrowser
from TFSA import delay


def seperator():
    """Prints a separator line to enhance readability."""
    print("-" * 110)


# Define tax information dictionaries
federal_tax = {
    0: [0, 15000],
    15.0: [15001, 53359],
    20.5: [53360, 106717],
    26.0: [106718, 165430],
    29.0: [165431, 235675],
    33.0: [235676, float('inf')]  # Assume no upper limit for the highest bracket
}

provincial_taxes = {
    "Newfoundland and Labrador": {
        0: [0, 10382],
        8.7: [10382, 41457],
        14.5: [41458, 82913],
        15.8: [82914, 148027],
        17.8: [148028, 207239],
        19.8: [207240, 264750],
        20.8: [264751, 529500],
        21.3: [529501, 1059000],
        21.8: [1059001, float('inf')]
    },
    "Prince Edward Island": {
        0: [0, 11250],
        9.8: [11250, 31984],
        13.8: [31985, 63969],
        16.7: [63970, float('inf')]
    },
    "Quebec": {
        0: [0, 17183],
        15: [17183, 49276],
        20: [49277, 98542],
        24: [98543, 119910],
        25.75: [119910, float('inf')]
    },
    "Nova Scotia": {
        0: [0, 11481],
        8.79: [11481, 29590],
        14.95: [29590, 59180],
        16.67: [59180, 93000],
        17.5: [93000, 150000],
        21: [150001, float('inf')]
    },
    "New Brunswick": {
        0: [0, 11599],
        9.4: [11599, 47715],
        14: [47715, 95431],
        16: [95431, 176756],
        19.5: [176756, float('inf')]
    },
    "Ontario": {
        0: [0, 11865],
        5.05: [11865, 49231],
        9.15: [49231, 98463],
        11.16: [98463, 150000],
        12.16: [150000, 220000],
        13.16: [220000, float('inf')]
    },
    "Manitoba": {
        0: [0, 10855],
        10.8: [10855, 36842],
        12.75: [36842, 79625],
        17.4: [79625, float('inf')]
    },
    "Saskatchewan": {
        0: [0, 16615],
        10.5: [0, 49720],
        12.5: [49720, 142058],
        14.5: [142058, float('inf')]
    },
    'Alberta': {
        0: [0, 20531],
        10: [20531, 148269],
        12: [148270, 177922],
        13: [177923, 237230],
        14: [237231, 355845],
        15: [355846, float('inf')]
    },
    "British Columbia": {
        0: [0, 11980],
        5.06: [11980, 45654],
        7.7: [45654, 91310],
        10.5: [91310, 104835],
        12.29: [104835, 127299],
        14.7: [127299, 172602],
        16.8: [172602, 240716],
        20.5: [240716, float('inf')]
    },
    "Yukon": {
        0: [0, 15000],
        6.4: [15001, 53359],
        9: [53359, 106717],
        10.9: [106717, 165430],
        12.8: [165430, 500000],
        15: [500000, float('inf')]
    },
    "Northwest Territories": {
        0: [0, 16593],
        5.9: [16594, 48326],
        8.6: [48326, 96655],
        12.2: [96655, 157139],
        14.05: [157139, float('inf')]
    },
    "Nunavut": {
        0: [0, 17925],
        4: [17925, 50877],
        7: [50877, 101754],
        9: [101754, 165429],
        11.5: [165429, float('inf')]
    }
}


def province_list():
    """ Printing the list of provinces in Canada """
    province_names = list(provincial_taxes.keys())

    seperator()
    print("Province Names: \n")
    for province_ in province_names:
        print("- {}".format(province_))
    seperator()


# Class calculating taxes and holding person's information
class Person:

    def __init__(self, province_name: str, net_income: int):
        # Class attributes
        self.province = province_name
        self.income = net_income

    # Calculating Federal Tax
    def federal_tax_calc(self, print_=True):
        if print_:
            seperator()
            print("Calculating Federal Taxes: ", end=" ")
            print("\n\n")

        federal_tax_amount = 0
        for tax_rate, income_range in federal_tax.items():
            if self.income > income_range[1]:
                federal_tax_amount += (income_range[1] - income_range[0]) * (tax_rate / 100)
                individual_fed_tax = (income_range[1] - income_range[0]) * (tax_rate / 100)
                if print_:
                    print("Tax : {0:5} %, Income Range: {1:16}, Federal Tax: {2:<11,.2f}".
                          format(tax_rate, str(income_range), individual_fed_tax))
            else:
                federal_tax_amount += (self.income - income_range[0]) * (tax_rate / 100)
                individual_fed_tax_2 = (self.income - income_range[0]) * (tax_rate / 100)
                if print_:
                    print("Tax : {0:5} %, Income Range: {1:16}, Federal Tax: {2:<11,.2f}".
                          format(tax_rate, str(income_range), individual_fed_tax_2))
                    print("\nFederal tax for 2023 at income of ${:,.2f} is: ${:,.2f}"
                          .format(self.income, federal_tax_amount))
                return federal_tax_amount

    # Calculating Provincial Tax
    def provincial_tax_calc(self, print_=True):
        if print_:
            seperator()
            print("Calculating Provincial Taxes: ", end=" ")
            print("\n\n")

        provincial_tax_amount = 0
        if self.province in provincial_taxes:
            for tax_rate, income_range in provincial_taxes[self.province].items():
                if self.income > income_range[1]:
                    provincial_tax_amount += (income_range[1] - income_range[0]) * (tax_rate / 100)
                    individual_prov_tax = (income_range[1] - income_range[0]) * (tax_rate / 100)
                    if print_:
                        print("Tax : {0:5} %, Income Range: {1:16}, Provincial Tax: {2:<11,.2f}".
                              format(tax_rate, str(income_range), individual_prov_tax))
                else:
                    provincial_tax_amount += (self.income - income_range[0]) * (tax_rate / 100)
                    individual_prov_tax_2 = (self.income - income_range[0]) * (tax_rate / 100)
                    if print_:
                        print("Tax : {0:5} %, Income Range: {1:16}, Provincial Tax: {2:<11,.2f}".
                              format(tax_rate, str(income_range), individual_prov_tax_2))
                        print("\nProvincial tax for 2023 at income of ${:,.2f} is: ${:,.2f}"
                              .format(self.income, provincial_tax_amount))
                        seperator()
                    return provincial_tax_amount

    # Comparing taxes of all the provinces
    def comparison(self):

        province_comparison = {}
        feds_tax = self.federal_tax_calc(print_=False)

        for province_ in provincial_taxes:
            provincial_tax_amount_ = 0
            for tax_rate_, income_range_ in provincial_taxes[province_].items():
                if income > income_range_[1]:
                    provincial_tax_amount_ += (income_range_[1] - income_range_[0]) * (tax_rate_ / 100)
                else:
                    provincial_tax_amount_ += (income - income_range_[0]) * (tax_rate_ / 100)
                    break
            province_comparison[province_] = income - (provincial_tax_amount_ + feds_tax)

        # Sort the dictionary in descending order based on values
        sorted_province_comparison = dict(
            sorted(province_comparison.items(), key=lambda item: item[1], reverse=True))

        # Print the sorted dictionary
        seperator()
        print("With annual income of: {:,.2f}, "
              "you will be left with the following money with respect to the province: \n".
              format(income))
        print("Province                  |  Money left after taxes:")
        for province__, money_left in sorted_province_comparison.items():
            print("{0:25} |  {1:,.2f}".format(province__, money_left))
        seperator()


income = 0
province = ""


def taxes_func():
    global province, income

    province_list()

    province = input("\nFrom above list, enter exact spelling of your province of residence: ")

    while province not in provincial_taxes:
        print("\nKindly enter the exact spelling of Province. First letters should be capital")
        province = input("From above list, enter exact spelling of your province of residence: ")

    while True:
        try:
            income = int(input("Enter your total annual income: "))
            break  # Exit the loop if successful conversion
        except ValueError:
            print("\nInvalid input. Please enter a numerical value for your income.")

    person1 = Person(province, income)
    fd_tax = person1.federal_tax_calc()
    delay()
    print("\n\n")
    pv_tax = person1.provincial_tax_calc()
    delay()
    print("\n\n")

    print("Income                 : $ {0:,.2f}".format(person1.income))
    print("Total Tax paid         : $ {0:,.2f}".format(pv_tax + fd_tax))
    print("Money left after taxes : $ {0:,.2f}".format(person1.income - (pv_tax + fd_tax)))
    print("\nPlease note that the above calculations does not include CPP (Canada Pension Plan) calculations.")
    seperator()

    print()
    user_answer = input("Would you like to see how much tax people pay with your salary in other provinces? [Y/N]: ")

    if user_answer == "Y" or user_answer == "y":
        person1.comparison()

    elif user_answer == "N" or user_answer == "n":
        print("I'm with you. I also don't want to feel sad knowing people in other provinces pay less taxes than me.")
    else:
        print("Do not try to be over-smart")

    user_input = input("\nDo you want to open the YouTube video to understand how taxes are calculated? [Y/N]: ")
    if user_input.lower() == 'Y' or user_input.lower() == 'y':
        webbrowser.open("https://www.youtube.com/watch?v=dZhpt887QP0&t=187s")
        print("Opening YouTube...")
    elif user_input.lower() == 'N' or user_input.lower():
        print("Okay, not opening the video for you.")
    else:
        print("Enter either 'Y' or 'N' next time.")
    seperator()
