#La Universidad del Valle requiere un programa que le permita conocer cómo califican los
#estudiantes la comida de la cafetería central. Para ello definió una escala de 1 a 10 (1 denota
#horrible y 10 denota excelente). El programa debe ser capaz capturar la calificación de
#cualquier número de estudiantes (no se sabe cuántos estudiantes se encuestarán, así que
#cuando el encuestador ingrese la calificación de 0, se sabrá que la encuesta habrá concluido).
#El programa deberá mostrar en su salida cuántos estudiantes fueron encuestados, así como el
#resumen de la encuesta como el promedio y cuál es la nota más alta dada y la nota más baja
#dada en la encuesta efectuada.

calificacion = int(input("calificacion : "))
cont = 0 

for i in range (0):
    while True:

        if calificacion  <= cont:
            print ("no hay calificacion  :" )
        

        elif calificacion >= 10:
            print ("calificacion excelente")
        
        elif calificacion < 10:
            print ("calificacion insuficiente : ")
        break




 