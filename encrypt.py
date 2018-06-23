from Crypto.Cipher import AES
from base64 import b64encode, b64decode

BLOCK_SIZE = 16

PADDING = '{'

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

def encrypt(key, msg):
	cipher = AES.new(pad(key).encode('utf-8'))
	return b64encode(cipher.encrypt(pad(msg))).decode('utf-8')

def decrypt(key, msg):
	cipher = AES.new(pad(key).encode('utf-8'))
	return cipher.decrypt(b64decode(msg)).decode('utf-8').rstrip(PADDING)

