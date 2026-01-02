from flask import Flask, render_template, request, jsonify
import base64
import requests
import hashlib
import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

app = Flask(__name__)

# CONFIGURATION
SIGNATURE = "encrizh"
priv_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
pub_key = priv_key.public_key()

def vigenere_logic(text, key, mode='encrypt'):
    key = key.upper()
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            if mode == 'decrypt': shift = -shift
            start = 65 if char.isupper() else 97
            result += chr((ord(char) - start + shift) % 26 + start)
        else: result += char
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_network')
def get_network():
    try:
        res = requests.get('https://ipapi.co/json/').json()
        return jsonify({"ip": res.get("ip"), "city": res.get("city"), "country": res.get("country_name"), "isp": res.get("org")})
    except:
        return jsonify({"ip": "127.0.0.1", "city": "Local", "country": "Offline", "isp": "Localhost"})

@app.route('/execute', methods=['POST'])
def execute():
    start_time = time.time()
    msg = request.form.get('message')
    algo = request.form.get('algo')
    
    # Hash Integrity
    msg_hash = hashlib.sha256(msg.encode()).hexdigest()
    secured_msg = f"{SIGNATURE}|{msg}"
    
    if algo == 'rsa':
        enc = pub_key.encrypt(secured_msg.encode(), padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        final = base64.b64encode(enc).decode()
    elif algo == 'vigenere':
        proc = vigenere_logic(secured_msg, SIGNATURE)
        final = base64.b64encode(proc.encode()).decode()
    else:
        proc = "".join([chr(ord(c) + 3) for c in secured_msg])
        final = base64.b64encode(proc.encode()).decode()

    speed = (time.time() - start_time) * 1000
    return jsonify({"result": final, "hash": msg_hash, "speed": f"{speed:.2f}ms", "sig": SIGNATURE})

if __name__ == '__main__':
    app.run(debug=True)