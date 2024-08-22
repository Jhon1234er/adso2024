from  loco.persona import*

per1 = persona('Pepe ', 672342 ,1500000)
per2 = persona('Carlos ', 43434 ,650000)
per3 = persona('Tiago ', 341232 , 3000000)
per4 = persona('Ana ', 43434 , 2000000)


def datosPersona(person):
    return f'{person.getNombre()}Con documento: {person.getDocumento()} Tiene de Salario :  {person.getSalario()} '

def instanciarObjeto(nombre,documento):
    return persona(nombre,documento)

print(datosPersona(per3))
print(datosPersona(per4))

# retornado=instanciarObjeto('Julio Iglesias',565656,1500000)
# print(type(retornado))
# print(retornado.getNombre())

#FUNCION PARA CALCULAR BASE DE COTIZACION
def calcularBase(person):
    return person.getSalario()*0.40

print(f'Base de cotización= {calcularBase(per3)}')

#EL 12% DE SALUD DE LA BASE DE COTIZACION

def SalarioSalud(person):
     return calcularBase(person)*0.12
print(f'Salud= {SalarioSalud(per3)}')

# EL 16% DE PENSION DE LA BASE DE COTIZACION

def SalarioPension(person):
    return calcularBase(person)*0.16
print(f'SalarioPension= {SalarioPension(per3)}')

# FUNCION INCREMENTO QUE AUMENTA EL SALARIO SEGUN EL PROCENTAJE COMO PARAMETROS RECIBE (PERSONA Y PROCENTAJE) Y RETORNA A LA PERSONA CON SALARIO NUEVO

def incrementarSalario(person, porcentaje):
    nuevoSalario = person.getSalario() + (person.getSalario() * porcentaje / 100)
    person.setSalario(nuevoSalario)
    return person
print (f'La persona {datosPersona(per3)} Y Tuvo un Incremento de Salario del= {incrementarSalario(per3, 10).getSalario()}')
0