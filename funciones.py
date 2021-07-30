def menu_y_seleccion():
  print('-------------------------------------------')
  print("Menu")
  print("1. Imprimir número de estudiantes")
  print("2. Agregar un estudiante")
  print("3. Buscar un estudiante por su nombre")
  print("4. Eliminar un estudiante por su documento")
  print("5. Mostrar todos los estudiantes")
  print("99. Salir del programa")
  print('-------------------------------------------')
  print()
  opcion = input('Ingrese selección: ')
  print()
  return opcion

def crear_estudiante():
  nombre = input('Nombre del estudiante: ')
  apellido = input('Apellido del estudiante: ')
  documento = input('Documento del estudiante: ')
  sexo = input('Sexo del estudiante: ')
  return {
      'nombre': nombre,
      'apellido': apellido,
      'documento': documento,
      'sexo': sexo,
  }

def buscar_estudiante_por_nombre(estudiantes, nombre_a_buscar):
  for estudiante in estudiantes:
    nombre_diccionario = estudiante['nombre']
    if (nombre_diccionario == nombre_a_buscar):
      return estudiante

def buscar_estudiante_por_documento(estudiantes, documento_a_buscar):
  for estudiante in estudiantes:
    if (estudiante['documento'] == documento_a_buscar):
      return estudiante
