from flask import Flask, request, jsonify
import os

app = Flask(__name__)

orders = {
    101: {"item": "Laptop", "status": "Pending"},
    102: {"item": "Phone", "status": "Shipped"},
    103: {"item": "Tablet", "status": "Delivered"}
}

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()

    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404

    orders[order_id]["status"] = data.get("status", orders[order_id]["status"])

    return jsonify({
        "message": "Order updated successfully",
        "order": orders[order_id]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
