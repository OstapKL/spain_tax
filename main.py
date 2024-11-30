import csv

# income ranges and corresponding tax percentage
taxes = {
    60000: 0.45,
    35200: 0.37,
    20200: 0.3,
    12450: 0.24,
    0: 0.19,
}


def calculate_income(brutto):
    netto = 0
    leftover = brutto
    for limit, tax in taxes.items():
        if leftover > limit:
            netto += (leftover - limit) * (1 - tax)
            leftover = limit

    return netto, brutto - netto


def write_income(file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Salary, €', 'Tax, %', 'Tax, €', 'Income, €'])
        step = 100
        for salary in range(step, 10000 + step, step):
            gross = salary * 12
            income, tax = calculate_income(gross)
            writer.writerow([salary, round(tax / gross * 100, 2), round(tax), round(income)])


if __name__ == '__main__':
    write_income('data.csv')
