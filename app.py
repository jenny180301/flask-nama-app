
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Render Flask App!"

@app.route("/tambah", methods=["POST"])
def tambah():
    nama = request.form.get("nama", "")
    return f"Nama diterima: {nama}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
