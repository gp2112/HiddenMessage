from flask import Flask, render_template, request, redirect, jsonify
from os import urandom
from binascii import hexlify
from encrypt import encrypt, decrypt
from model import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/send', methods=['POST'])
def save():
	message = request.form['message']
	key = request.form['key']
	link = hexlify(urandom(8)).decode('utf-8')
	encrypt_msg = encrypt(key, message)
	save_msg(link, encrypt_msg)
	return render_template('success.html', link=link, key=key)

@app.route('/msg/<link>')
def get_message(link):
	if link not in get_msgs():
		return 'Message not found', 404
	return render_template('get_msg.html', link=link)

@app.route('/decrypt/<content>')
def decrypt_msg(content):
	link = content.split('-')[0]
	key = content.split('-')[1]
	cripto_msg = get_msgs()[link]
	try:
		msg = decrypt(key, cripto_msg)
	except UnicodeDecodeError:
		return 'wrong key', 404
	delete_msg(link)
	return msg

@app.route('/api')
def api():
	msgs = get_msgs()
	return jsonify(msgs)

app.run(debug=True)

