#importando o panda e o re para trabalhar com expressões regulares
import re
import pandas as pd

# Função para validar e-mail
def validate_email(email):

    if pd.isna(email):
        return False
    
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zAZ0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))

# Função para validar CPF
def validate_cpf(cpf: str) -> bool:

    if pd.isna(cpf):
        return False
    
    numbers = [int(digit) for digit in cpf if digit.isdigit()]
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False
    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False
    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False
    return True

# Função para formatar telefone
def format_phone(phone):
    
    if pd.isna(phone):
        return False
    
    phone = re.sub(r'[^0-9]', '', phone)
    if len(phone) == 11:
        return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"


# Função para formatar data
def format_date(date):
    if pd.isna(date):
        return False
    try:
        return pd.to_datetime(date).strftime('%d/%m/%Y')
    except ValueError:
        return None
