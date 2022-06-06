

import matplotlib.pyplot as plt 
import libreria.clases as lb
import numpy as np

fig=plt.figure(figsize=(12,8), constrained_layout=True)
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0])

datos=[]

f=open("C:/Users/santiago/OneDrive/Desktop/Parcial 3 programación- Santiago Castaño/Aspirantes_Doctorados_Exterior_2010_-_2016.csv",encoding="utf8")
        #dentro de las comillas ingrese la ruta en la que esta el archivo .csv
#El siguiente ciclo ingresa los datos de el archivo .csv a la lista datos
for k in f:
    datos.append(k.split(","))
f.close()


años_str=['2010','2011','2012','2013','2014','2015','2016']
años=[2010,2011,2012,2013,2014,2015,2016]
años_cuadrado=[2010**2,2011**2,2012**2,2013**2,2014**2,2015**2,2016**2]
masculinos=[]
femeninos=[]

for j in años_str:
    a=lb.datos(j,'MASCULINO',0,datos).contar()
    b=lb.datos(j,'FEMENINO',0,datos).contar()
    masculinos.append(a)
    femeninos.append(b)


ax1.plot(años,masculinos,"o-",color="b",label="hombres")
ax1.plot(años,femeninos,"o-",color="r",label="mujeres")
ax1.grid(True)
ax1.legend()
ax1.set_title("COLOMBIANOS ASPIRANTES A DOCTORADOS EN EL EXTRANJERO")
ax1.set_xlabel("AÑO")
ax1.set_ylabel("NÚMERO DE PERSONAS")

x=np.linspace(2010,2020,8)

regre_masc=lb.predict(años,masculinos,años_cuadrado).regresion()
regre_fem=lb.predict(años,femeninos,años_cuadrado).regresion()
y1=regre_masc[0]*x+regre_masc[1]
y2=regre_fem[0]*x+regre_fem[1]
ax1.plot(x,y1,"o-",label="regresión hombres")
ax1.plot(x,y2,"o-",label="regresión mujeres")

ax1.legend()
plt.show()

    
    
    
    
