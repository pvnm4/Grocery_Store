def get_units(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM units")
    cursor.execute(query)
    responce = []
    for (unit_id,unit_name) in cursor:
        responce.append({
            'unit_id': unit_id,
            'unit_name':unit_name
        })
    return responce

if __name__ == '__main__':
    from backend.app.prev.sql_connection import get_sql_connection

    connection = get_sql_connection()
    print(get_units(connection))