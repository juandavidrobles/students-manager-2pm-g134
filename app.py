from funciones import buscar_estudiante_por_documento, buscar_estudiante_por_nombre, crear_estudiante, menu_y_seleccion
import time

estudiantes = [
  {
    'nombre': 'sebas',
    'apellido': 'correa',
    'documento': '64435',
    'sexo': 'm',
  },
  {
    'nombre': 'martin',
    'apellido': 'martinez',
    'documento': '644435',
    'sexo': 'm',
  },
  {
    'nombre': 'daniela',
    'apellido': 'porras',
    'documento': '64433',
    'sexo': 'f',
  },
]
while True:
  opcion = menu_y_seleccion()
  if (opcion == '1'):
    print(f"Cantidad de estudiantes: {len(estudiantes)}")
  elif (opcion == '2'):
    estudiante = crear_estudiante()
    estudiantes.append(estudiante)
    print('\nEstudiante creado con éxito\n')
  elif (opcion == '3'):
    nombre_a_buscar = input('Ingrese el nombre del estudiante a buscar: ')
    estudiante_encontrado = buscar_estudiante_por_nombre(estudiantes, nombre_a_buscar)
    if (estudiante_encontrado == None):
      print('No se encontró ningun estudiante')
    else:
      print(estudiante_encontrado)
  elif (opcion == '4'):
    documento_a_buscar = input('Ingrese documento del estudiante a buscar: ')
    estudiante_encontrado = buscar_estudiante_por_documento(estudiantes, documento_a_buscar)
    if (estudiante_encontrado == None):
      print('No se encontró ningún estudiante con el documento ingresado')
    else:
      estudiantes.remove(estudiante_encontrado)
      print('Estudiante eliminado exitosamente')
  elif (opcion == '5'):
    for estudiante in estudiantes:
      print(estudiante)
  elif (opcion == '99'):
    print('Cerrando programa...')
    print('Hasta luego')
    break
  else:
    print('Opción no válida')

  time.sleep(2)
