from backend.app.prev.sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT  products.product_id, products.name , products.unit_id ,products.price_per_unit ,units.unit_name FROM products inner join units on units.unit_id=products.unit_id;")
    cursor.execute(query)
    responce = []
    for (product_id,name,unit_id,price_per_unit,unit_name) in cursor:
        responce.append({
            'product_id': product_id,
            'name': name,
            'unit_id':unit_id,
            'price_per_unit':price_per_unit,
            'unit_name':unit_name
        })
        
    cursor.close()
    return responce


def insert_new_product(connection,product):
    cursor = connection.cursor()

    query = ("insert into products (name, unit_id, price_per_unit) VALUES(%s,%s,%s)")
    data = (product['product_name'],product['unit_name'],product['price_per_unit'])

    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection,product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    # print(insert_new_product(connection, {
    #     'product_name':'tomato',
    #     'unit_name':'2',
    #     'price_per_unit':'30'
    # }))
    #print(get_all_products(connection))
    print(delete_product(connection,8))