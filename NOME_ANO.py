while True:
    nome = str(input("Qual seu nome? "))
    try:
        if nome.isalpha() == False or nome == '':
            raise ValueError('Nome inválido! Digite apenas letras e espaços!')
        else:
            break
    except ValueError as e:
        print(f'Erro: {e}')
    
while True:
    ano_nascimento = str(input ("Digite o ano que você nasceu c/ 4 digitos, entre 1922 e 2022: "))
    try:
        if ano_nascimento.isnumeric() == False or ano_nascimento == '':
            raise ValueError("Data precisa ser um número de 4 dígitos")
        else:
            ano = int(ano_nascimento)
            if (ano < 1922 or ano > 2022):
                raise ValueError("Data errada, digite um ano entre 1922 e 2022")
            else:
                break
    except ValueError as e:
        print(f'Erro: {e}')
    
idade = 2023 - ano
print("Você estará com ",idade," anos em 2023")