# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database sementara dalam memori
devices = []

@app.route('/api/devices', methods=['POST'])
def add_device():
    # TODO: Mahasiswa harus mengimplementasikan logika di sini:
    # 1. Ambil JSON dari request
    # 2. Validasi apakah field 'name' dan 'ip_address' ada. Jika tidak, return 400.
    # 3. Validasi apakah 'ip_address' sudah ada di list 'devices'. Jika ya, return 409 (Conflict).
    # 4. Jika valid, simpan ke 'devices' dan return 201.
    pass

@app.route('/api/devices', methods=['GET'])
def get_devices():
    return jsonify(devices), 200

if __name__ == '__main__':
    app.run(debug=True)
