import random
from difflib import get_close_matches

# Federal tax brackets
federal_tax_brackets = [
    (55867, 0.15),
    (111733, 0.205),
    (173205, 0.26),
    (246752, 0.29),
    (float('inf'), 0.33)
]

# Provincial tax rates
provincial_tax_rates = {
    "alberta": [(142292, 0.1), (170751, 0.12), (227668, 0.13), (341502, 0.14), (float('inf'), 0.15)],
    "british columbia": [(45654, 0.0506), (91310, 0.077), (104835, 0.105), (127299, 0.1229), (172602, 0.147),
                         (240716, 0.168), (float('inf'), 0.205)],
    "manitoba": [(36842, 0.108), (79625, 0.1275), (float('inf'), 0.174)],
    "new brunswick": [(47715, 0.094), (95431, 0.14), (176756, 0.16), (float('inf'), 0.195)],
    "newfoundland and labrador": [(41457, 0.087), (82913, 0.145), (148027, 0.158), (207239, 0.178), (264750, 0.198),
                                  (529500, 0.208), (1059000, 0.213), (float('inf'), 0.218)],
    "northwest territories": [(48326, 0.059), (96655, 0.086), (157139, 0.122), (float('inf'), 0.1405)],
    "nova scotia": [(29590, 0.0879), (59180, 0.1495), (93000, 0.1667), (150000, 0.175), (float('inf'), 0.21)],
    "nunavut": [(50877, 0.04), (101754, 0.07), (165429, 0.09), (float('inf'), 0.115)],
    "ontario": [(49231, 0.0505), (98463, 0.0915), (150000, 0.1116), (220000, 0.1216), (float('inf'), 0.1316)],
    "prince edward island": [(31984, 0.098), (63969, 0.138), (float('inf'), 0.167)],
    "quebec": [(49275, 0.14), (98540, 0.19), (119910, 0.24), (float('inf'), 0.2575)],
    "saskatchewan": [(49720, 0.105), (142058, 0.125), (float('inf'), 0.145)],
    "yukon": [(53359, 0.064), (106717, 0.09), (165430, 0.109), (500000, 0.128), (float('inf'), 0.15)]
}


def calculate_taxable_income(taxable_income, brackets):
    total_tax = 0
    remaining_income = taxable_income
    for bracket in brackets:
        if remaining_income <= 0:
            break
        bracket_amount, tax_rate = bracket
        if remaining_income <= bracket_amount:
            total_tax += remaining_income * tax_rate
            break
        else:
            total_tax += bracket_amount * tax_rate
            remaining_income -= bracket_amount
    return total_tax


def calculate_rrsp_contribution(yearly_income, start_year, retirement_year, salary_growth_rate):
    table = []
    salary = yearly_income
    contribution_rate = 0.06
    employer_contribution_rate = 0.04
    total_contributions = 0
    total_returns = 0
    rrsp_account = 0

    for year in range(start_year, retirement_year + 1):
        employee_contribution = salary * contribution_rate
        employer_contribution = salary * employer_contribution_rate
        total_contribution = employee_contribution + employer_contribution
        total_contributions += total_contribution
        rate_of_return = random.uniform(0.03, 0.05) * total_contribution
        total_returns += rate_of_return
        rrsp_account += total_contribution + rate_of_return
        table.append([year, salary, employee_contribution, employer_contribution, total_contribution, rate_of_return,
                      rrsp_account])
        salary *= (1 + min(salary_growth_rate, 5) / 100)

    return table, total_contributions, total_returns, rrsp_account


def calculate_tfsa_contribution(yearly_income, start_year, retirement_year, salary_growth_rate):
    table = []
    salary = yearly_income
    contribution_rate = 0.08
    total_contributions = 0
    total_returns = 0
    tfsa_account = 0

    for year in range(start_year, retirement_year + 1):
        employee_contribution = salary * contribution_rate
        total_contributions += employee_contribution
        rate_of_return = random.uniform(0.03, 0.05) * employee_contribution
        total_returns += rate_of_return
        tfsa_account = employee_contribution + rate_of_return
        table.append([year, salary, employee_contribution, rate_of_return, tfsa_account])
        salary *= (1 + min(salary_growth_rate, 5) / 100)

    return table, total_contributions, total_returns, tfsa_account


def print_table(table, title):
    print(f"\n{title}:")
    print("{:<10} {:<15} {:<25} {:<30} {:<25}".format("Year", "Salary/Income", "Contribution", "Return on Investment",
                                                      "Total Amount"))
    for row in table:
        print("{:<10} ${:<15.2f} ${:<25.2f} ${:<30.2f} ${:<25.2f}".format(*row))


def rrsp_func():
    yearly_income = float(input("Enter your yearly income: "))
    start_year = int(input("Enter the year you started working: "))
    max_retirement_year = start_year + 40
    retirement_year = int(input(f"Enter your expected year of retirement (max {max_retirement_year}): "))
    retirement_year = min(retirement_year, max_retirement_year)

    salary_growth_rate = float(input("Enter the rate at which your salary will grow annually (max 5%) (%): "))

    rrsp_table, rrsp_total_contributions, rrsp_total_returns, rrsp_final_amount = calculate_rrsp_contribution(
        yearly_income, start_year, retirement_year, salary_growth_rate)
    print_table(rrsp_table, "RRSP Details")

    print(
        f"\nYour yearly salary started in {start_year} and grew at an annual rate of {salary_growth_rate}%, "
        f"until the year {retirement_year}. You contributed a total of ${rrsp_total_contributions:.2f} "
        f"into your RRSP Account.")
    print(
        f"At an average annual return rate of 3% to 5%, you can expect to earn approximately ${rrsp_total_returns:.2f} "
        f"across {retirement_year - start_year + 1} years.")
    print(f"The total amount in your RRSP Account at the end of {retirement_year} would be ${rrsp_final_amount:.2f}.")

    province_input = input("Enter your province: ").lower()
    suggested_province = get_close_matches(province_input, provincial_tax_rates.keys(), n=1, cutoff=0.7)
    if suggested_province and suggested_province[0] != province_input:
        confirm = input(f"Did you mean {suggested_province[0]}? Enter 'y' or 'n': ")
        if confirm.lower() == 'y':
            province_input = suggested_province[0]

    provincial_tax_brackets = provincial_tax_rates.get(province_input)

    if provincial_tax_brackets is None:
        print("Province not found. Cannot calculate taxes.")
        return

    federal_tax = calculate_taxable_income(rrsp_total_returns, federal_tax_brackets)
    provincial_tax = calculate_taxable_income(rrsp_total_returns, provincial_tax_brackets)
    total_tax_deduction = federal_tax + provincial_tax

    rrsp_after_tax = rrsp_final_amount - total_tax_deduction

    print(f"\nFederal Tax Deduction: \033[90m${federal_tax:.2f}\033[0m")
    print(f"Provincial Tax Deduction ({province_input.title()}): \033[90m${provincial_tax:.2f}\033[0m")
    print(f"Total Tax Deduction: \033[90m${total_tax_deduction:.2f}\033[0m")
    print(f"\nAmount left after tax deduction for RRSP: \033[90m${rrsp_after_tax:.2f}\033[0m")

    show_tfsa_details = input("Do you want to see the TFSA details? (y/n): ").lower()
    if show_tfsa_details == 'y':
        tfsa_table, tfsa_total_contributions, tfsa_total_returns, tfsa_final_amount = calculate_tfsa_contribution(
            yearly_income, start_year, retirement_year, salary_growth_rate)
        print_table(tfsa_table, "TFSA Details")

        print(f"\nYou contributed a total of ${tfsa_total_contributions:.2f} into your TFSA Account.")
        print(
            f"At an average annual return rate of 3% to 5%, you can expect to earn approximately "
            f"${tfsa_total_returns:.2f} across {retirement_year - start_year + 1} years.")
        print(
            f"The total amount in your TFSA Account at the end of {retirement_year} would be ${tfsa_final_amount:.2f}.")

        federal_tax_tfsa = calculate_taxable_income(tfsa_total_returns, federal_tax_brackets)
        provincial_tax_tfsa = calculate_taxable_income(tfsa_total_returns, provincial_tax_brackets)
        total_tax_deduction_tfsa = federal_tax_tfsa + provincial_tax_tfsa

        tfsa_after_tax = tfsa_final_amount - total_tax_deduction_tfsa

        print(f"\nFederal Tax Deduction for TFSA: \033[90m${federal_tax_tfsa:.2f}\033[0m")
        print(
            f"Provincial Tax Deduction for TFSA ({province_input.title()}): \033[90m${provincial_tax_tfsa:.2f}\033[0m")
        print(f"Total Tax Deduction for TFSA: \033[90m${total_tax_deduction_tfsa:.2f}\033[0m")
        print(f"\nAmount left after tax deduction for TFSA: \033[90m${tfsa_after_tax:.2f}\033[0m")


if __name__ == "__main__":
    rrsp_func()
