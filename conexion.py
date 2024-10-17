import mysql.connector
import pandas as pd
try : 
    from scraping import  Titulo_Producto
    from scraping import  Especificacion
    from scraping import  precio_producto
    from scraping import  url_img

    print(Titulo_Producto.text)
except : 
    print("Se ha producido un error en la ejecución del programa. Intentando nuevamente...")

    
try : 
    conexion = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'jhan1040',
        database = 'webscraping'
        )
    cursor = conexion.cursor()
    consulta = 'INSERT INTO Elementos(TituloProducto,Especificaciones,precioProducto,urlImg)VALUES(%s,%s,%s, %s)'
    Datos_insertar =(f"{Titulo_Producto.text}", 
                  f"{Especificacion.text}", 
                  f"{precio_producto.text}",
                  f"{url_img}")
    cursor.execute(consulta,Datos_insertar)
    conexion.commit()
    print(cursor.rowcount, "registro insertado")

except :
    print("Error al momento de insertar")
# La insercion a la base esta funcinando correctamente  



def dataframe() :
    try : 
        consulta_de_selecionarDatos = 'SELECT * FROM Elementos'
        cursor.execute(consulta_de_selecionarDatos)
        resultados = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(resultados, columns=columnas)
        print(df)
        cursor.close()
        conexion.close()
    except :
        print("Error al momento de crear el Dataframe")

dataframe()

 

