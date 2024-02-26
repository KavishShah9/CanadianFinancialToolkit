def advisory_func():
    print("WEALTHSIMPLE EXPLAINS: SHOULD I INVEST IN AN RRSP OR A TFSA?")
    employer_matching = input("Does your employer offer RRSP matching? (y/n): ").lower()

    if employer_matching == "y":
        print("Take the maximum free money every year. It's part of your salary!")
        ask_debt()
    else:
        ask_debt()


def ask_debt():
    debt = input("Before you go any further, do you have debt? (y/n): ").lower()

    if debt == "n":
        ask_emergency_fund()
    else:
        print(
            "For example, high-interest rate debt could "
            "be credit cards, while low-interest rate debt could be mortgages.")
        debt_type = input("Enter 1 if you have high-interest rate debt, or 2 if you have low-interest rate debt: ")
        if debt_type == "1":
            print("STOP! Use any spare cash to eliminate your debt.")
        else:
            ask_emergency_fund()


def ask_emergency_fund():
    emergency_fund = input("Do you have an emergency fund? (y/n): ").lower()

    if emergency_fund == "n":
        print("STOP! Use any spare cash to start an emergency fund.")
    else:
        print("Great, you have some money to invest.")
        ask_income()


def ask_income():
    income = input("Now, do you earn more than $50,000 per year? (y/n): ").lower()

    if income == "n":
        print("Start contributing to TFSA.")
    else:
        ask_high_income()


def ask_high_income():
    income = input("Do you earn more than $100,000 per year? (y/n): ").lower()

    if income == "n":
        anticipate_high_income()
    else:
        anticipate_low_income()


def anticipate_high_income():
    anticipate = input(
        "Do you anticipate that your annual income will be more than"
        " $100,000 per year in the next 3 years? (y/n): ").lower()

    if anticipate == "y":
        print("Contribute to your TFSA first until it's maxed out.")
    else:
        contribute_rrsp()


def anticipate_low_income():
    anticipate = input(
        "Do you anticipate that your annual income will be more than $100,000 per year "
        "in the next 3 years? (y/n): ").lower()

    if anticipate == "y":
        contribute_rrsp()
    else:
        print("Contribute to your TFSA until it's maxed out.")
        contribute_rrsp()


def contribute_rrsp():
    withdrawal_income = input(
        "When the time comes to withdraw funds, do you think your income "
        "will be lower than it is today? (y/n): ").lower()

    if withdrawal_income == "y":
        print(
            "Contribute to an RRSP. You'll save money on your taxes now, and you'll "
            "pay lower taxes on that cash when you withdraw it in retirement.")
    else:
        print("Contribute to your TFSA until it's maxed out. Then start making RRSP contributions.")


if __name__ == "__main__":
    advisory_func()
