#Hecho por Erasmo Villarreal Sánchez A01197677
#Examen de Lectura para PISA
from time import *

#Lecturas almacenadas
lectura1 ='''La ceramica de Puebla \n 
La fabricación de la cerámica de Puebla era bastante sencilla.
Los barros que se empleaban provenían de las cercanías de la ciudad de Puebla;
el blanco de San Bartolo, y el rojo y el negro, de los cerros de Loreto y Guadalupe.
Mezclados en partes iguales, era batida la amalgama por los pisadores, después
de haberse eliminado las asperezas causadas por basuras o cuerpos extraños. 
Se ponía al sol, y después se depositaba en un lugar húmedo durante cinco o seis
meses, tiempo durante el cual adquiría el barro la necesaria plasticidad para su 
manipulación. Entonces se moldeaban los objetos ya fuera a mano o por medio de un
torno, y después de secarse completamente en lugares abrigados, se sometían al 
fuego del primer horno, llamado *jaguete, operación que era generalmente procedida
por una pequeña ceremonia: reunía el maestro del *alfar, enfrente de la boca del 
horno, a todos los oficiales, aprendices y operarios; permanecían todos descubiertos
por algun tiempo, en religioso tiempo y después el maestro pronunciaba con toda 
solemnidad las palabras: "¡Alabado sea por siempre el Santísimo Sacramento!" y daba
fuego al horno. Esta ceremonia se repetía al abrirse el horno para sacarse las 
piezas ya cocidas. Los hornos para esta primera cochura eran generalmente cuadrados
y de pequeñas dimensiones: se usaba leña común y duraba la cocción de seis a siete 
horas. 

*jaguete: horno
*alfar: obrero de alfarero

Romero, M cit en Kabalen, D. y de Sánchez, M. (2006)
'''

lectura2 = '''Efectos de la radiación sobre las mujeres embarazadas \n
Si una mujer embarazada se expone a la radiación existe una probabilidad
relativamente alta de causar serios daños al embrión, que podrían llevarlo 
hasta la muerte y subsecuentemente ocasionar un aborto, o bien la aparición 
de mal formaciones en el recién nacido (efecto llamado teratogénesis). 
Los estudios con animales han demostrado que la radiación produce la 
disminución en el tamaño de la cabeza (microcefalia) y alteraciones en la 
formación del esqueleto del ser irradiado en el útero. Los estudios en aquellos
sobrevivientes que se encontraban en el útero durante las explosiones de 
Hiroshima y Nagasaki han mostrado que tienen menor estatura, alcanzan un peso 
menor, y sus diametros cefálicos son inferiores a los del grupo testigo no 
irradiado. 

Se sabe con certeza que el embrión es mas sensible a los efectos teratogénicos
de los virus, de algunas sustacias químicas y la de radiación, durante ciertas
etapas de su desarrollo uterino. Había 22 individuos, que se encontraban antes
de su semana 18 de gestación al ser irradiados en Hiroshima y Nagasaki. 
De ellos, 13 nacieron con microcefalia y 8 sufrieron retraso mental. La dosis
estimada de todos los casos fue superior a los 150 rems. Para dosis inferiores
a 50 rems no se encontraron malformaciones en el grupo estudiado. 

Los estudios con animales muestran que dosis tan bajas como de unos pocos rems
durante etapas críticas del desarrollo embrionario pueden causar malformaciones

Kabalen, D. y de Sánchez, M. (2006) La Lectura analítico-crítica. Edit. Trillas: 
México. 
'''
#Aquí almaceno las respuestas
respuestasLec1 =["b","a","d","a","b"]
respuestasLec2 =["c","c","a","d","a"]
oracionesCorrectas = ["Ella quiere comprar el libro", "El mal del cáncer causa un dolor intenso y acaba por invadir los huesos", "El perro y el delfín son los mejores amigos del ser humano", "Hasta mañana estarán el análisis y la solución del caso por la tarde", "Cantar ayuda a sentirse alegre"]
oracionesIncorrectas = ["comprar libro ella quiere el", "acaba por el mal dolor del cáncer invadir y causa los huesos un intenso", "el delfín amigos y son los mejores del perro del ser humano","estarán mañana hasta el análisis y la solución por la tarde del caso","ayuda el a alegre sentirse cantar"]
preLec1 = ["1. La palabra 'aprendices', linea 10 significa: \na)aprendizajes\nb)principiantes\nc)cómplices\nd)artesanos","2. El tema del texto es: \na)el arte de la cerámica\nb)ceramistas\nc)los tesoros de Puebla\nd)artesanos","3. ¿Cuál sería la idea central del texto leído?: \na)es importante la limpieza del barro antes de trabajarlo\nb)los grandes privilegios de la ciudad de Puebla\nc)El sacramento que representa prender el horno\nd)la fabricación de la cerámica es un arte","4. ¿Cuál es el propósito del autor: \na)Informar\nb)Organizar\nc)Instruir\nd)Persuadir","¿5. Cómo presenta el autor la información: \na)hechos e inferencias\nb)hechos\nc)inferencias y opiniones\nd)opiniones"]
preLec2 = ["1. El tema del texto es: \na)la mujer\nb)la mujer embarazada\nc)radiación\nd)efecto de la guerra", "2. ¿Cuál sería la idea central del texto leído? : \na)los cuidados que debe de tener una mujer embarazada\nb)las consecuencias desastrosas de las guerras nucleares\nc)consecuencias que causa la radiación durante el embarazo\nd)investigaciones con animales de los efectos radioactivos", "3. ¿Cuál es el propósito del autor: \na)informar\nb)modificar\nc)instruir\nd)persuadir", "4. El tono del autor es: \na)sarcástico\nb)inquisitivo\nc)depresivo\nd)neutro", "5. El tipo de lenguaje que utiliza el autor: \na)objetivo\nb)subjetivo"]

correctas = 0 #este es el numero de correctas
veces = 1 #el numero de veces que se ha hecho el examen
def displayOraciones(oracionesIncorrectas): #esta función es para que las oraciones se impriman en el shell
    resOraciones= []
    for i in range(0,len(oracionesIncorrectas)):
        print("Oración #",i+1)
        print(oracionesIncorrectas[i],"\n")
        res = input("Ordena correctamente la frase anterior (Escribe con mayúscula al principio de cada oración ): ")
        print("")
        resOraciones.append(res)
    return resOraciones

def checkListas(alumno, sistema): #aquí se comprueban las respuestas de las oraciones para ver si están correctamente ordenadas
    global correctas
    for i in range(0, len(sistema)):
        if alumno[i]== sistema[i]:
            correctas += 1
    return correctas

def dispPreguntas(preLec): #aquí se imprimen las preguntas de las lecturas, todas las preguntas se imprimen con esta función
    resLec = []
    for i in range(0,5):
        print(preLec[i])
        respuestas="" #también aquí se aceptas las respuestas
        while respuestas!="a" or respuestas!="b" or respuestas!="c" or respuestas!="d":
            respuestas = input("Inserta el inciso de tu respuesta: ")
            if respuestas=="a" or respuestas=="b" or respuestas=="c" or respuestas=="d":
                resLec.append(respuestas)
                break
            else:
                respuestas = input("Respuesta invalida inserta el inciso de tu respuesta: ")
                if respuestas=="a" or respuestas=="b" or respuestas=="c" or respuestas=="d":
                    resLec.append(respuestas)
                    break
        print("")
        
    return resLec
def checkDiccio(correc,listaRes): #aquí es donde se checa que el se haya escogido el inciso correcto de la pregunta
    global correctas
    for i in range(0,5):
        if correc[i] == listaRes[i]:
            correctas+=1
    return correctas

def main():
    
    global correctas
    print("                      ")
    print("Examen de practica PISA")
    nombre = input("Escribe tu nombre: ")
    print("Bienvenido", nombre) #El usuario da su nombre
    tiempoInicial = time() #Empieza a contarse el tiempo
    resAlumno = displayOraciones(oracionesIncorrectas) #se imprimen las oraciones incorrectas, y se optiene una lista con las respuestas
    correctas += checkListas(resAlumno,oracionesCorrectas) #las oraciones son calificadas y se acumulan las correctas
    print("")
    print("Siguiente sección, Lectura comprensiva.\n")

    print(lectura1)
    resLec1 = dispPreguntas(preLec1) #se imprimen las preguntas y se aceptan las respuestas previamente validadas dentro de la funcion
    correctas += checkDiccio(respuestasLec1,resLec1) #se acumulan las oraciones correctas
    #se hace lo mismo que en las 3 lineas anteriores
    print(lectura2)
    resLec2 = dispPreguntas(preLec2) 
    correctas += checkDiccio(respuestasLec2,resLec2)

    
    tiempoFinal = time() #se deja de contar el tiempo
    tiempoTotal = tiempoFinal-tiempoInicial #se saca el tiempo total
    print(round(tiempoTotal,2)," Total de tiempo en segundos") 

    #se le da una recompensa de puntos a la persona que participe en el examen de acuerdo al tiempo que se tardó
    if tiempoTotal <= 200:
        correctas += 5
    elif tiempoTotal >= 200 and tiempoTotal<= 300:
        correctas+= 2
    print ("Puntaje",correctas*5)
    if correctas >= 20:
        print("Muchas felicidades, puedes descansar.")
    elif correctas > 15 and correctas <20:
        print("Casi lo logras, síguelo intentando...")
    else: 
        print("Sigue practicando")

#Esta es la parte final, donde se corre el main code, y despues se pregunta al usuario si quiere volver a empezar el examen
empezar = True
main()
while empezar == True:
    seguir = input("Quieres repetir el examen? s/n: ")
    if seguir== "s":
        correctas = 0
        veces +=1
        main()
    elif seguir =="n":
        print("")
        print("¡Esperamos que te haya sido de gran ayuda este examen para prepararte!")
        empezar = False
    else:
        print("Respuesta invalida")
    if empezar == False:
        break
print("¡Mucho éxito!")
print("Lo intentaste",veces,"veces")

