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

    for sales in data:
        if product_key in sales:
            total += sales[product_key]
    return total
    pass



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
    total_sales_a=0
    total_sales_b=0
    total_sales_c=0
    for i in data:
        total_sales_a += i["product_a"]
        total_sales_b += i["product_b"]
        total_sales_c += i["product_c"]
        if total_sales_a > total_sales_b and total_sales_a > total_sales_c:
            return "product_a"
        elif total_sales_b > total_sales_a and total_sales_b > total_sales_c:
            return "product_b"
        else:
            return "product_c"
    pass

def worst_selling_day(data):
    """Finds the day with the lowest total sales."""
    if not data:
        return None  
    worst_day = data[0]["day"]
    min_sales = data[0]["product_a"] + data[0]["product_b"] + data[0]["product_c"]
    
    for day_data in data[1:]:  
        total_sales = day_data["product_a"] + day_data["product_b"] + day_data["product_c"]
        if total_sales < min_sales:
            min_sales = total_sales
            worst_day = day_data["day"]
    return worst_day
    pass

def top_3_days(data):
    """Sorts days by total sales and shows the top 3."""
    list_total_sales = []

    for i in data:
        total_sales = i["product_a"] + i["product_b"] + i["product_c"]
        list_total_sales.append((i["day"], total_sales))
    list_total_sales.sort(key=lambda x: x[1], reverse=True)
    return list_total_sales[:3]

def sales_range(data, product_key):
    """Calculates the sales range (max - min) of a product."""
    min_ventas = float("inf")  
    max_ventas = float("-inf")

    for i in data:
        ventas = i[product_key]
        if ventas < min_ventas:
            min_ventas = ventas
        if ventas > max_ventas:
            max_ventas = ventas

    return max_ventas - min_ventas



# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_b"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest totagit pushl sales:", top_product(sales_data))
print("Day with lowest total sales:", worst_selling_day(sales_data))
print("Top 3 total sales sorted by days", top_3_days(sales_data))
print("Sales range (max - min) of a product:",sales_range(sales_data, "product_c"))
