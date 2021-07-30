file = open('./text.txt', 'a')

entrada = input('Ingrese texto: ')

file.write('\n' + entrada)