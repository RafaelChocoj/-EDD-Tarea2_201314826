import os

def pedir_matris(x_tipo):
    col = input("Ingrese no.Columnas (x) ")
    fil = input("Ingrese no.filas (y) ")
    input("matriz ingresada: "+ str(col) + "," + str(fil))

    input("cordenada a linealizar")
    i = input("Ingrese (i) ")
    j = input("Ingrese (j) ")
    input("linealizar a : "+ str(i) + "," + str(j))

    if x_tipo == "x_fila":
        k = int(i)*int(col) + int(j)
        print("POR FILA - posicion: " +str(k))

    if x_tipo == "x_colum":
        k = int(j)*int(fil) + int(i)
        print("POR COLUMNA - posicion: " +str(k))

    graf_linea(int(col), int(fil), int(i) , int(j) , x_tipo)


def graf_linea(col_x, fil_y, i , j, x_tipo):
    f = open("linea.txt", "w")
    
    f.write("digraph G { rankdir=LR\n")
    f.write("node [shape=record style=filled];\n")
    ###
    for y in range(0, fil_y):
        for x in range(0, col_x):

            if i == x and j == y:
                
                f.write("p"+str(x)+str(y)+"[label=\"{<data> ("+str(x)+","+str(y)+") |<next>}\" pos=\""+str(x)+","+str(y)+"!\" fillcolor=\"#1f77b4\"];\n")
            else:
                f.write("p"+str(x)+str(y)+"[label=\"{<data> ("+str(x)+") |<next>}\" pos=\""+str(x)+","+str(y)+"!\"];\n")
                    
    f.write("}")
    f.close()
    
    os.system("fdp -Tpng linea.txt -o linea.jpg")
    os.system("linea.jpg")

    if x_tipo == "x_fila":
        k = int(i)*int(col_x) + int(j)

        f1 = open("fila.txt", "w")
    
        f1.write("digraph G { rankdir=LR\n")
        f1.write("node [shape=record style=filled];\n")
        ###
        for y in range(0, 1):
            for x in range(0, col_x * fil_y):

                if k == x:
                    f1.write("p"+str(x)+str(y)+"[label=\"{<data> ("+str(x)+") |<next>}\" pos=\""+str(x)+","+str(y)+"!\" fillcolor=\"#1f77b4\"];\n")
                else:
                    f1.write("p"+str(x)+str(y)+"[label=\"{<data> ("+str(x)+") |<next>}\" pos=\""+str(x)+","+str(y)+"!\"];\n")
                        
        f1.write("}")
        f1.close()
    
        os.system("fdp -Tpng fila.txt -o fila.jpg")
        os.system("fila.jpg")


    elif x_tipo == "x_colum":
        k = int(j)*int(fil_y) + int(i)
        f2 = open("colum.txt", "w")
    
        f2.write("digraph G { rankdir=LR\n")
        f2.write("node [shape=record style=filled];\n")
        ###
        for y in range(0, col_x * fil_y):
            for x in range(0, 1):

                if k == y:
                    f2.write("p"+str(x)+str(y)+"[label=\"{<data> ("+str(y)+") |<next>}\" pos=\""+str(x)+","+str(y)+"!\" fillcolor=\"#1f77b4\"];\n")
                else:
                    f2.write("p"+str(x)+str(y)+"[label=\"{<data> ("+str(y)+") |<next>}\" pos=\""+str(x)+","+str(y)+"!\"];\n")
                        
        f2.write("}")
        f2.close()
    
        os.system("fdp -Tpng colum.txt -o colum.jpg")
        os.system("colum.jpg")






if __name__ == "__main__":

    bolano = True
    while(bolano):
        print("\n\n\n")
        print("****Menu****")
        print("1.- mapeo Filas\n"+
        "2.- mapeo Columna\n"+
        "3.- Salir\n")
        op = input("seleccione opcion para poder continuar: ")
        if op == "1":
            pedir_matris("x_fila")
            
        elif op == "2":
            pedir_matris("x_colum")
        elif op == "3":
            bolano = False