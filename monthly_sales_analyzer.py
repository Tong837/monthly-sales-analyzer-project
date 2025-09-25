# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total=0
    #Recorro las ventas en la data especificada en el print.
    for sales in data:
        #Condiciono que el producto que especificaremos este en data¿?
        if product_key in sales:
            #Acumulo las ventas del procuto que se especifica en print()
            total += sales[product_key]
    return total
    pass
#print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))


def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total_sales = total_sales_by_product(data, product_key)
    #porque len(data) en number_of_days -- ¿CÓMO SÉ QUE LEN(DATA) ME CALCULA EL NUMERO DE DIAS? ¿DE DONDE SACA LA INFO? ¿LEE CUANTAS LINEAS TIENE EL DICCIONARIO?
    number_of_days = len(data)  #¿LEE CUANTAS FILAS HAY EN LA DATA? POR ESO ME DEVUELVE 20 DIAS?
    average = total_sales / number_of_days 
    
    #Me aseguro de que devuelva algo en el caso de que la lista no tenga datos
    if number_of_days > 0:
        return average
    else:
        return 0
    pass


"""average=0
    total_days=20
    for i in data:
        average +=i[product_key]/total_days
    return average
    pass """


def best_selling_day(data):
    """Finds the day with the highest total sales."""
   #Esta función funcionara especificamente para la lista "sales_data" ya que le estoy pasando los parametros concretos (key) del nombre de los productos. 
   #Hago que busque coincidencias de las calves para  extraer los valores(value) en ese diccionario concreto.

    best_day=""
    max_sales=0
    for i in data:
        #SUMO TODOS LAS VENTAS DE TODOS LOS PRODUCTS
        total_sales_by_day = i["product_a"]+i["product_b"]+i["product_c"]

        if total_sales_by_day > max_sales:
            max_sales = total_sales_by_day #NO ENTIENDO BIEN ESTA PARTE ¿QUÉ APORTA AL CONDICIONAL?
            best_day = i["day"] #Le indico dónde buscar el día de mejor venta apartir del cúmulo de las ventas totales 
            
    return best_day
    pass
#print("Day with highest total sales:", best_selling_day(sales_data))
#Day with highest total sales: 12

def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    counter=0
    for days in data:
        if days[product_key] > threshold:
            counter +=1
    return counter
    pass
#print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
#El valor threshold te lo da el print como parámetro al pasar la función: 300
#Days when product_c exceeded 300 sales: 8 DIAS DEL TOTAL DE 20 LAS VENTAS HAN SUPERADO 300€

def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    #Inicializo las variables para acumular el total de las ventas de los productos
    total_sales_a=0
    total_sales_b=0
    total_sales_c=0
    #Con el bucle recorro la lista y acumulo en las variables el total de cada producto haciendo llamada a cada key específica de la lista.
    for i in data:
        total_sales_a += i["product_a"]
        total_sales_b += i["product_b"]
        total_sales_c += i["product_c"]
        #Aplico estructura de condicionales usando los operadores lógicos(>) y de expresión (and). 
        #En cada vuelta del condicional clasificará las ventas según el número más alto.
        if total_sales_a > total_sales_b and total_sales_a > total_sales_c: #Si producto a es mayor a b y c entonces devuelve producto a
            return "product_a"
        elif total_sales_b > total_sales_a and total_sales_b > total_sales_c: #Aquí ya sabemos que si se ejecuta este elif, el producto a no será el de mayor ventas
            return "product_b"
        else: #Si ninguna de las otras conciones se cumple, entonces el total mayor de ventas será el producto c
            return "product_c"
    pass

def worst_selling_day(data):
    """Finds the day with the lowest total sales."""
    if not data: #Me aseguro de qué la función devuelva un resultado en el caso de que la lista este vacía (if not data in data...)
        print ("No hay datos en la lista") 
   
    #Con data me refiero al diccionario dado "sales_data" y [0] marca el primer elemento del diccionario y asi tendremos el valor de esa "key"("day")
    #Inicializo esta variable como el primer peor día
    worst_day = data[0]["day"] 
    #En esta variable acumulo la suma total de las ventas de cada producto de todos los dias para averiguar cual será la venta mas baja
    min_sales = data[0]["product_a"] + data[0]["product_b"] + data[0]["product_c"]
    
    #Creo el bucle para comparar por días el total_sales con las min_sales por día
    for day_data in data:
        #Creo otra variable con la misma suma de datos para poder compararlos en el condicional  
        total_sales = day_data["product_a"] + day_data["product_b"] + day_data["product_c"]
       #Si las ventas totales son menores a las ventas mínimas el total sales pasará a ser la venta mínima.
        if total_sales < min_sales:
            min_sales = total_sales #Aquí se actualiza el valor mínimo seteando a través del bucle que ese peor día pertece al día checkeado cada línea de código
                                    #Solo si el dia que comprueba tiene total_sales menores al dato de la actualización anterior
            worst_day = day_data["day"] #Al actualizarse min_sales como el bucle recorre el diccionario por filas, este entenderá que la ultima actu de min_sales 
                                        #Es también el peor día ya que he escrito esa linea justo debajo, este condional condiciona las tres variables y actualiza min_sales a la par de worst_day
    return worst_day
    pass

def top_3_days(data):
    """Sorts days by total sales and shows the top 3."""
    #Creo una lista vacía para acumulas los datos y poder filtrar los tres mejores resultados
    list_total_sales = []

    #Recorro el diccionario acumulando la suma de las ventas generales
    for i in data:
        total_sales = i["product_a"] + i["product_b"] + i["product_c"] #¿PODRÍA UTILIZAR TOTAL_SALES.SUM(DATA)?
        list_total_sales.append((i["day"], total_sales)) #Aquí relleno la lista vacía. Añadiendo con la función .append una tupla dentro de la lista
    list_total_sales.sort(key=lambda x: x[1], reverse=True) #Con la función .sort ordeno los datos. Utilizo lambda para poder ordenar los datos en una sola linea de código.
                                                            #Aplicando lamdba a key le digo que trabaje con elemto x y le especifico la posición del elemento (el segundo elemento [1])
                                                            #Reverse=True, ya que por defecto (false) los datos se ordenan de ascendente necesito cambiar ese orden de mayor a menor
   #Filtro la lista al devolver los datos. "[:3]"" saca los 3 primeros datos que ya estan ordenados de froma descendente.
    return list_total_sales[:3]

def sales_range(data, product_key):
    """Calculates the sales range (max - min) of a product."""
    #Como no sé cuál puede ser el max de ventas inicializo la variable con un float infito negativo ¿PORQUE EL INFINITO NEGATIVO ENCUENTRA EL MAX?
    min_ventas = 0  
    max_ventas = float("-inf")

    #Para la info en la data las ventas serán los valores del producto (no entiendo bien que seria product_key, ¿COGE EL VALOR DE LA KEY?)
    for i in data:
        ventas = i[product_key]
        #Condiciono que ese cumulo de ventas y se actalizan dentro de la variable ¿Si encontramos un valor menor o mayor al anterior comparado?
        if ventas < min_ventas:
            min_ventas = ventas
        if ventas > max_ventas:
            max_ventas = ventas
    #Calculamos el rango, que será la diferencia entre el mínimo y el máximo para saber cuánto varian las ventas de un producto
    #Si el rango es bajo, las ventas del producto serán estables. Al contrario si el rango es alto significa que el producto se vende de forma irregular.
    return max_ventas - min_ventas



# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest totagit pushl sales:", top_product(sales_data))
print("Day with lowest total sales:", worst_selling_day(sales_data))
print("Top 3 total sales sorted by days", top_3_days(sales_data))
print("Sales range (max - min) of a product:",sales_range(sales_data, "product_c"))
