import random
import re

def generate_random_cnpj_numbers():
    return [random.randint(0, 9) for _ in range(12)]

def calculate_verification_digits(cnpj_digits):
    # Calculate the first verification digit
    total = sum((cnpj_digits[i] * (5 - i) for i in range(4))) + \
            sum((cnpj_digits[i] * (9 - i) for i in range(4, 12)))
    first_verification_digit = 11 - total % 11
    if first_verification_digit >= 10:
        first_verification_digit = 0
    cnpj_digits.append(first_verification_digit)

    # Calculate the second verification digit
    total = sum((cnpj_digits[i] * (6 - i) for i in range(5))) + \
            sum((cnpj_digits[i] * (9 - i) for i in range(5, 13)))
    second_verification_digit = 11 - total % 11
    if second_verification_digit >= 10:
        second_verification_digit = 0
    cnpj_digits.append(second_verification_digit)

def format_cnpj(cnpj_digits):
    cnpj = ''.join(str(digit) for digit in cnpj_digits)
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

def generate_random_cnpj(num_cnpjs):
    cnpjs = []
    for _ in range(num_cnpjs):
        cnpj_digits = generate_random_cnpj_numbers()
        calculate_verification_digits(cnpj_digits)
        cnpj_with_format = format_cnpj(cnpj_digits)

        # Use regex to extract only the numbers from the formatted CNPJ
        cnpj_numbers_only = re.sub(r'\D', '', cnpj_with_format)

        cnpjs.append(cnpj_numbers_only)

    return cnpjs

# Test the function with generating 5 CNPJs
num_cnpjs = 5
generated_cnpjs = generate_random_cnpj(num_cnpjs)
print("Generated CNPJs:", generated_cnpjs)
