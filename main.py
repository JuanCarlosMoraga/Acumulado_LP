import os
import dao.daoConnection as dao
import models.clases 

os.system('cls')
conex = dao.Connection("localhost", "root", "", "dbregisters")
conex.connect()

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
'''daoCity.insert(city1)
daoCity.insert(city2)
daoCity.insert(city3)
daoCity.insert(city4)
daoCity.insert(city5)
daoCity.insert(city6)'''
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