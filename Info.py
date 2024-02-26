from Advisory import advisory_func


def show_tfsa_info():
    print("Tax-Free Savings Account (TFSA) Information:")
    print("- A TFSA is a registered account that allows Canadians to earn tax-free investment income.")
    print("- Contributions to a TFSA are made with after-tax dollars, and any investment income, including capital "
          "gains and dividends, earned within the account is tax-free.")
    print("- Unused TFSA contribution room can be carried forward indefinitely.")
    print("- The annual TFSA contribution limit is determined by the government and may change from year to year.")
    print("For more information, enter 'm'.")
    print()


def show_fhsa_info():
    print("First Home Savings Account (FHSA) Information:")
    print("- The FHSA is designed to help Canadians save for their first home.")
    print("- Contributions to an FHSA are not tax-deductible, but investment income "
          "earned within the account is tax-free.")
    print("- Withdrawals from an FHSA can only be used towards the purchase of a first home.")
    print("- The FHSA program has specific eligibility criteria and contribution limits set by the government.")
    print("For more information, enter 'm'.")
    print()


def show_rrsp_info():
    print("Registered Retirement Savings Plan (RRSP) Information:")
    print("- An RRSP is a tax-advantaged account designed to help Canadians save for retirement.")
    print("- Contributions to an RRSP are tax-deductible, meaning they can reduce your taxable income for the year.")
    print("- Investment income earned within an RRSP, including interest, dividends, "
          "and capital gains, grows tax-deferred until withdrawal.")
    print("- Withdrawals from an RRSP are taxed as income in the year they are withdrawn.")
    print("For more information, enter 'm'.")
    print()


def info_func():
    print("Welcome to the Canadian Investment Account Information Program!\n")
    while True:
        print("Choose an option to view information:")
        print("1. TFSA (Tax-Free Savings Account)")
        print("2. FHSA (First Home Savings Account)")
        print("3. RRSP (Registered Retirement Savings Plan)")
        print("4. Financial Advisory")
        print("5. References")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        print()
        if choice == '1':
            show_tfsa_info()
            more_info = input("Enter 'm' for more information, or press Enter to continue: ")
            if more_info.lower() == 'm':
                print("- TFSA withdrawals are tax-free and can be made at any time for any purpose.")
                print("- Common TFSA investment options include savings "
                      "accounts, GICs, stocks, bonds, and mutual funds.")
                print("- The rate of return for TFSA investments can vary "
                      "depending on the chosen investment vehicles and market conditions.")
                print()
        elif choice == '2':
            show_fhsa_info()
            more_info = input("Enter 'm' for more information, or press Enter to continue: ")
            if more_info.lower() == 'm':
                print("- Unused FHSA contribution room can be carried forward for up to 15 years.")
                print("- Common FHSA investment options include high-interest savings accounts, GICs, "
                      "and conservative investments.")
                print("- The rate of return for FHSA investments can vary depending on the chosen investment vehicles "
                      "and market conditions.")
                print()
        elif choice == '3':
            show_rrsp_info()
            more_info = input("Enter 'm' for more information, or press Enter to continue: ")
            if more_info.lower() == 'm':
                print("- RRSP contribution room is based on your earned income and any unused"
                      " contribution room can be carried forward indefinitely.")
                print("- Common RRSP investment options include mutual funds, ETFs, stocks, bonds, and GICs.")
                print("- The rate of return for RRSP investments can vary depending on the chosen"
                      " investment vehicles and market conditions.")
                print()

        elif choice == '4':
            advisory_func()

        elif choice == '5':
            print("References:")
            print("1. TFSA - Tax-Free Savings Account: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4466/tax-free-savings-account-tfsa-guide-individuals.html")
            print("2. FHSA - First Home Savings Account: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account.html")
            print("3. RRSP - Registered Retirement Savings Plan: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/registered-retirement-savings-plan-rrsp.html")
            print("4. Difference Between TFSA, RRSP, and FHSA: https://protectyourwealth.ca/difference-between-tfsa-rrsp-fhsa/#:~:text=The%20FHSA%20is%20a%20combination,unlike%20withdrawals%20from%20an%20RRSP.")
            print()

        elif choice == '6':
            print("Thank you for using the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-5).\n")

        another_choice = input("\nWould you like to select another option? (y/n): ")
        if another_choice.lower() != 'y':
            print("Thank you for using the program. Goodbye!")
            break
        print()


if __name__ == "__main__":
    info_func()
