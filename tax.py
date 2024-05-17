'''A module to calculate Tax'''
TAX=0.1

def tax_to_pay():
    '''This function calculates the tax payable with a tax rate of 10%'''
    salary=float(input("Enter your salary: "))
    tax_payable=salary*TAX
    return tax_payable


print(tax_to_pay())
print(TAX)
