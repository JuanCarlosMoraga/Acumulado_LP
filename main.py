import os
import dao.daoConnection as dao
import models.clases 

os.system('cls')
conex = dao.Connection("localhost", "root", "", "dbregisters")
conex.connect()

'''
#instanciar modelo
city1 = models.clases.City("Chontales", 1)
city2 = models.clases.City("León", 1)
city3 = models.clases.City("Granada", 1)
city4 = models.clases.City("Masaya", 1)
city5 = models.clases.City("Estelí", 1)
city6 = models.clases.City("Jinotepe", 1)

#instanciar dao
daoCity = dao.DaoCity(conex)
#insertar
daoCity.insert(city1)
daoCity.insert(city2)
daoCity.insert(city3)
daoCity.insert(city4)
daoCity.insert(city5)
daoCity.insert(city6)
#Eliminar
daoCity.delete(1)
daoCity.delete(2)
daoCity.delete(3)
daoCity.delete(4)
daoCity.delete(5)
daoCity.delete(6)


#consultar
cities = daoCity.get_all()
for city in cities:
    print(city)
'''
#Ciudad
def insertarCiudad():
    nombre = input("Nombre ciudad:")
    status = input("Inserte 0 o 1:")
    ciudad = models.clases.City(nombre, 1)
    daoCity = dao.DaoCity(conex)
    #insertar
    daoCity.insert(ciudad)
def mostrarCiudad():
    daoCity = dao.DaoCity(conex)
    cities = daoCity.get_all()
    for city in cities:
        print(city)

def editarCiudad():
    _id= input("digite el Id de la ciudad que desea editar: ")
    _name= input("digite el nombre de la ciudad: ")
    _status= input("digite el estatus: ")
    daoCity=dao.DaoCity(conex)
    daoCity.update(_name, _status, _id)

    a = daoCity.get_by_id(_id)
    print(a)
def eliminarCiudad():
    _id= input("digite el Id de la ciudad que desea eliminar: ")
    daoCity=dao.DaoCity(conex)
    daoCity.delete(_id)

def buscarCiudad():
    _id= input("digite el Id de la ciudad que desea buscar: ")
    daoCity=dao.DaoCity(conex)
    a = daoCity.get_by_id(_id)
    print(a)
#Empleados
def insertarEmpleado():
    print("***Digite los datos del Empleado***")
    first_name = input("Nombre: ")
    last_name = input("Apellido: ")
    city = input("Id ciudad: ")
    job = input("Id Puesto: ")
    salary = input("Salario: ")
    Employee = models.clases.Employee(first_name, last_name, city, job, salary, 1)
    daoEmployee = dao.DaoEmployees(conex)
    #insertar
    daoEmployee.insert(Employee)

def mostrarEmpleado():
    os.system("cls")
    daoEmployee=dao.DaoEmployees(conex)
    employees = daoEmployee.get_all()
    print("Lista de Empleados: ")
    for employee in employees:
        print(employee)

def editarEmpleado():
    os.system("cls")
    _id= input("digite el Id del empleado que desea editar: ")
    daoEmployee = dao.DaoEmployees(conex)
    a = daoEmployee.get_by_id(_id)
    print("Empleado seleccionado: ")
    print(a)

    first_name = input("Nombre: ")
    last_name = input("Apellido: ")
    city = input("Id ciudad: ")
    job = input("Id Puesto: ")
    salary = input("Salario: ")
    status = input("status: ")
    daoEmployee=dao.DaoEmployees(conex)
    Employee = models.clases.Employee(first_name, last_name, city, job, salary, status)
    daoEmployee.update(Employee, _id)

    b = daoEmployee.get_by_id(_id)
    print("Empleado editado exitosamente: ")
    print(b)

def eliminarEmpleado():
    _id= input("Digite el Id del empleado que desea borrar: ")
   
    daoEmployeee = dao.DaoEmployees(conex)
    a = daoEmployeee.get_by_id(_id)
    print("Empleado seleccionado: ")
    print(a)
   
    Employee = daoEmployeee.delete(_id)
    print(Employee)

def buscarEmpleado():
    _id= input("Digite el Id de la ciudad que desea mostrar: ")
    daoEmployee = dao.DaoEmployees(conex)
    Employee = daoEmployee.get_by_id(_id)
    print(Employee)

#Puesto de trabajo
def insertarPuesto():
    name = input("Nombre del puesto: ")
    job = models.clases.Job(name,1)
    daoJob = dao.DaoJobs(conex)
    #insertar
    daoJob.insert(job)

def mostrarPuestos():
    os.system("cls")
    daojob = dao.DaoJobs(conex)
    jobs = daojob.get_all()
    print("Lista de Puestos: ")
    for job in jobs:
        print(job)

def eliminarPuesto():
    _id= input("Digite el Id del puesto que desea borrar: ")
    daoJob = dao.DaoJobs(conex)
    a = daoJob.get_by_id(_id)
    print(a)
    Job = daoJob.delete(_id)
    print(Job)

def editarPuesto():
    os.system("cls")
    _id = input("Digite el Id del puesto que desea editar: ")
   
    daoJob=dao.DaoJobs(conex)
    a = daoJob.get_by_id(_id)
    print(a)

    _name= input("Digite el nombre del puesto: ")
    _status= input("Digite el estatus: ")
    daoJob=dao.DaoJobs(conex)
    Job = models.clases.Job(_name, _status)
    daoJob.update(Job, _id)

    b = daoJob.get_by_id(_id)
    print(b)

def buscarPuesto():
    _id= input("Digite el Id del puesto que desea mostrar: ")
    daoJob = dao.DaoJobs(conex)
    Job = daoJob.get_by_id(_id)
    print(Job)

#Menus principal
def menu():
    os.system("cls")
    print("***Menu Principal***")
    print("1. Menu ciudades")
    print("2. Menu Empleados")
    print("3. Menu Puestos")
    print("4. Salir")

def menuCiudad():
    print("***Menu Ciudad***")
    print("1. Ingresar ciudad")
    print("2. Editar ciudad")
    print("3. Mostrar ciudades")
    print("4. Eliminar ciudad")
    print("5. Buscar ciudad")
    print("6. Salir")

def menuJobs():
    print("***Menu Puestos***")
    print("1. Ingresar Puesto")
    print("2. Editar Puesto")
    print("3. Mostrar Puestos")
    print("4. Eliminar Puesto")
    print("5. Buscar Puesto")
    print("6. Salir")

def menuEmployee():
    print("***Menu Empleados***")
    print("1. Ingresar empleado")
    print("2. Editar empleado")
    print("3. Mostrar empleados")
    print("4. Eliminar empleado")
    print("5. Buscar empleado")
    print("6. Salir")

#Main de pantallas
def main():
    opcion = ""

    while opcion != "4":
        menu()
        opcion = input("Dime tu opcion: ")

        if opcion == "1":
            mainCiudad()
            os.system("pause")
        elif opcion == "2":
            mainEmployees()
            os.system("pause")
        elif opcion == "3":
            mainJobs()
            os.system("pause")
        elif opcion == "":
            menu()

def mainCiudad():
    opcion = ""

    while opcion != "6":
        os.system("cls")
        menuCiudad()
        opcion = input("Dime tu opcion: ")

        if opcion == "1":
            insertarCiudad()
            os.system("pause")
        elif opcion == "2":
            editarCiudad()
            os.system("pause")
        elif opcion == "3":
            mostrarCiudad()
            os.system("pause")
        elif opcion == "4":
            eliminarCiudad()
            os.system("pause")
        elif opcion == "5":
            buscarCiudad()
            os.system("pause")
        elif opcion == "":
            menuCiudad()

def mainJobs():
    opcion = ""

    while opcion != "6":
        os.system("cls")
        menuJobs()
        opcion = input("Dime tu opcion: ")

        if opcion == "1":
            insertarPuesto()
            os.system("pause")
        elif opcion == "2":
            editarPuesto()
            os.system("pause")
        elif opcion == "3":
            mostrarPuestos()
            os.system("pause")
        elif opcion == "4":
            eliminarPuesto()
            os.system("pause")
        elif opcion == "5":
            buscarPuesto()
            os.system("pause")
        elif opcion == "":
            menuJobs()

def mainEmployees():
    opcion = ""

    while opcion != "6":
        os.system("cls")
        menuEmployee()
        opcion = input("Dime tu opcion: ")

        if opcion == "1":
            insertarEmpleado()
            os.system("pause")
        elif opcion == "2":
            editarEmpleado()
            os.system("pause")
        elif opcion == "3":
            mostrarEmpleado()
            os.system("pause")
        elif opcion == "4":
            eliminarEmpleado()
            os.system("pause")
        elif opcion == "5":
            buscarEmpleado()
            os.system("pause")
        elif opcion == "":
            menuEmployee()
       

main()