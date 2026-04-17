from flask import Flask, render_template, request
import hashlib
import base64

app = Flask(__name__)

# ---------------------------
# XOR
# ---------------------------
def xor_process(text, key):
    data = bytes([b ^ key for b in text.encode("utf-8")])
    return base64.b64encode(data).decode()

def xor_decrypt(text, key):
    data = base64.b64decode(text)
    return bytes([b ^ key for b in data]).decode()

# ---------------------------
# HASH
# ---------------------------
def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

# ---------------------------
# WEB ROUTE
# ---------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    
    if request.method == "POST":
        text = request.form.get("text")
        key = request.form.get("key")

        if "crypt" in request.form:
            result = xor_process(text, int(key))

        elif "decrypt" in request.form:
            result = xor_decrypt(text, int(key))

        elif "hash" in request.form:
            result = sha256(text)

    return render_template("index.html", result=result)

# ---------------------------
# RUN
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)