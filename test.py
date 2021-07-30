import json

file = open('./data/estudiantes.txt', 'r')
file_content = file.read()
estudiantes = json.loads(file_content)

string = json.dumps(estudiantes)
print(type(string))