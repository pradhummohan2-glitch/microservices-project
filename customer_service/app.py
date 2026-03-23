from flask import Flask, jsonify
import os

app = Flask(__name__)

customers = {
    1: {"name": "Pradhum", "orders": [101, 102]},
    2: {"name": "Rahul", "orders": [103]}
}

orders = {
    101: {"item": "Laptop", "status": "Pending"},
    102: {"item": "Phone", "status": "Shipped"},
    103: {"item": "Tablet", "status": "Delivered"}
}

@app.route('/customers/<int:customer_id>/orders', methods=['GET'])
def get_customer_orders(customer_id):
    customer = customers.get(customer_id)

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    customer_orders = []
    for order_id in customer["orders"]:
        order = orders.get(order_id)
        if order:
            customer_orders.append({ "order_id": order_id, **order })

    return jsonify({
        "customer": customer["name"],
        "orders": customer_orders
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

@app.route('/')
def home():
    return "Customer Service is running"