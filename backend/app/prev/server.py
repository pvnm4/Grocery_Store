from flask import Flask, request, jsonify , json
from backend.app.prev.sql_connection import get_sql_connection
import backend.app.prev.products_dao as products_dao
import backend.app.prev.units_dao as units_dao

app = Flask(__name__)
connection = get_sql_connection()

@app.route('/getUnits',methods=['GET'])
def get_unit():
    units = units_dao.get_units(connection)
    responce =  jsonify(units)
    responce.headers.add('Access-Control-Allow-Origin','*')
    return responce


@app.route('/getProducts')
def get_products():
    products = products_dao.get_all_products(connection)
    responce =  jsonify(products)
    responce.headers.add('Access-Control-Allow-Origin','*')
    return responce

@app.route('/insertProduct',method=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection,request_payload)
    responce = jsonify({
        'product_id':product_id
    })
    responce.headers.add('Access-Control-Allow-Origin','*')
    return responce

if __name__ == '__main__':
    print("Starting Python flask server for Grocery Store Management System")
    app.run(port=5000)