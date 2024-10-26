from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Membuat fungsi untuk mengambil harga barang dari database
def get_product_price(barcode):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM products WHERE barcode = ?", (barcode,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint untuk mengambil harga berdasarkan barcode
@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    barcode = data.get('barcode')
    price = get_product_price(barcode)
    
    if price:
        return jsonify({'price': price})
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
