#primeiro passo é importar a biblioteca pandas
import pandas as pd
#Aqui estou importando as funções que irei utilizar
from funcoes import *

# Esta linha de cod interpetra o arquivo csv que foi fornecido...
df_desafio = pd.read_csv('desafio.csv', dtype=str)

# Aqui vou criar uma lista para armazenar os dados 
dados = []

# Esse for vai percorrer cada item do arquivo fornecido para que eu possa aplicar as alterações solicitadas linha por linha
for index, row in df_desafio.iterrows():

    # Nome para title
    name = row['Nome'].title()
    
    # validando E-mail
    if validate_email(row['E-mail']) == True:
        email = row['E-mail']
    else:
        email = ""

    # Telefone formatado 
    phone = format_phone(row["Celular"])
    
    # Data de nascimento fofrmatado
    birthdate = format_date(row['Data de Nascimento'])

    # CPF validado 
    if validate_cpf(row['CPF']) == True:
        cpf = row['CPF'] 

    else:
        cpf = ""
    
    # Endereço 1
    address_1 = row['Endereco'] 
    
    # Endereço 2 (não existe match)
    address_2 = '' 
    
    # CEP (somente números)
    zipcode = row['CEP'].replace("-", "").strip() 
    
    # Estado
    state = row['UF']
    
    # Cidade
    city = row['Cidade']
    
    # Bairro
    district = row['Bairro']
    
    # Nome do responsável
    contact_name = row['Responsavel'] if pd.isna(row['Responsavel']) else row['Responsavel'].title()

    # CPF do responsável (validado)
    if validate_cpf(row['CPF Responsavel']) == True:
        contact_cpf = row['CPF Responsavel']
    else: 
        contact_cpf = ""
    
    # Aqui vou adicionar os dados trocando cada um para seu correspondente... 
    dados.append({
        'name': name,
        'email': email,
        'phone': phone,
        'birthdate': birthdate,
        'cpf': cpf,
        'address_1': address_1,
        'address_2': address_2,
        'zipcode': zipcode,
        'state': state,
        'city': city,
        'district': district,
        'contact_name': contact_name,
        'contact_cpf': contact_cpf
    })

# Convertendo a lista de dicionários para um DataFrame
df_final = pd.DataFrame(dados, columns=['name', 'email', 'phone', 'birthdate', 'cpf', 'address_1', 'address_2', 'zipcode', 'state', 'city', 'district', 'contact_name', 'contact_cpf'])

# Salvar o resultado em um arquivo CSV
df_final.to_csv('desafio_final.csv', index=False)
 
#mostrando no terminal  resultado gerado...
print (df_final)

