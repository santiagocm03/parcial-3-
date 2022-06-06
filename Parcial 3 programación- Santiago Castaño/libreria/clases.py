import matplotlib.pyplot as plt
import numpy as np

#fig=plt.figure(figsize=(12,8), constrained_layout=True)
#gs=fig.add_gridspec(1,1)
#ax1=fig.add_subplot(gs[0,0])

class datos:
    def __init__(self,año,genero,lista,datos):
        self.año=año
        self.genero=genero
        self.datos=datos
    def __str__(self):
        return("|"+str(self.año)+"|"+str(self.genero)+"|"+str(self.lista)+"|"+str(self.datos)+"|")
    def __mul__(self,other):
        return([self.año,self.genero,self.lista,self.datos,other.año,other.genero,other.lista,other.datos])
    def __sub__(self,other):
        return(datos(self.año-other.año,str(self.genero)+"-"+str(other.genero),str(self.lista)+"-"+str(other.lista),str(self.datos)+"-"+str(other.datos)))
    def __add__(self,other):
        return(datos(self.año+other.año,self.genero+other.genero,str(self.lista)+"+"+str(other.lista),str(self.datos)+"+"+str(other.datos)))
    def sumaproducto(self,a,b):
        """
        Esta funcios suma el  producto de los componentes correspondientes
        de dos listas a y b, donde len(a)==len(b)
    
        a:list
        b:list
    
        >>>sumaproducto(años,masculinos)
        Returns:3713256
        """
        c=0
        for n in range(len(a)):
            c+=a[n]*b[n]
        return(c)
    def suma(self,lista):
        """
        Esta funcion suma todos los componentes de una lista
        
        lista:list
        
        >>>suma(años)
        Returns:14091
        
        """
        c=0
        for o in lista:
            c+=o
        return(c)
    def contar(self):
        
        """
        Esta función cuenta el numero de colombianos (MASCULINO O FEMENINO)
        que se postularon a un doctorado en el exterior entre '2010' y '2016'
        año : str
        el año se debe ingresar entre comillas sencillas, valido entre 2010 y 2016.
            genero : str
            el genero se debe ingresar en mayusculas y entre comillas sencillas.
            
            >>>contar('2010','MASCULINO')
            Returns:311

       """
        contador=0
        for i in range(len(self.datos)):
           if self.datos[i][1]==self.año and self.datos[i][3]==self.genero:
               contador+=1
        return(contador)

class predict(datos):
    def __init__ (self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __str__(self):
        return("*"+str(self.a)+"\n"+"*"+str(self.b)+"\n"+"*"+str(self.c))
    def __add__(self, other):
        A=[]
        B=[]
        C=[]
        for i in range(len(self.a)):
            A.append(self.a[i]+other.a[i])
            B.append(self.b[i]+other.b[i])
            C.append(self.c[i]+other.c[i])
        return(predict(A,B,C))
    def __setitem__(self,p,e):
        """
        Permite mutar la clase predict
        p:int (indica la posición en la que se va a añadir el dato)
        e:int (es el dato que se va a agregar en la posición p)
        """
        try:
            self.a[p]=e
            self.b[p]=e
            self.c[p]=e
        except:
            self.a.append(e)
            self.b.append(e)
            self.c.append(e)
    def __getitem__(self,p):
        """
        Permite itemizar la clase predict
        
        p:int (indica la posición del dato)

        """
        return(self.a[p],self.b[p],self.c[p])
    def regresion(self):
        """
        Esta función realiza una regresión lineal con las coordenadas
        de dos listas a y b donde len(a)==len(b) 
        
        a:list
        b:list
        c:list(corresponde a los cuadrados de la lista a)
        """
        
        m=((len(self.a)*super().sumaproducto(self.a,self.b))-(super().suma(self.b)*super().suma(self.a)))/((len(self.a)*(super().suma(self.c)))-(super().suma(self.a))**2)
        
        A=(super().suma(self.b)-(m*super().suma(self.a)))/len(self.a)
        
        r=[m,A]
        
        return(r)