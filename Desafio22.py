# Analizador de texto.
nome = str(input('Digite o seu nome: ')).strip() #Elimina espaços inúteis no começo e no final
print('O seu nome é {}'.format(nome))
print('Ao todo, o seu nome tem {} caracteres, incluido os espaços'.format(len(nome))) #Conta quantos caracteres tem, incluindo o espaço
print('Este é o seu nome em maiúsculas {}'.format(nome.upper())) #Deixa tudo em maiúscula
print('Este é o seu nome em minúsculas {}'.format(nome.lower())) #Deixa tudo em minúscula

altera = nome.replace(' ', '') #Elinima espaços
print('O seu nome tem ao todo {} letras'.format(len(altera)))

#Outra maneira de eliminar espaços:
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

corta = nome.split() #Divide por palavras e cria uma lista
print('O seu primeiro nome é {0} e ele tem {1} letras'.format(corta[0], len(corta[0])))

#Outra maneira de contar as letras do primeiro nome:
print('O seu primeiro nome é {0} e ele tem {1} letras'.format(corta[0], nome.find(' ')))