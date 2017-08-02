from SHA3 import *
from encryption import *
from scrambler import *
import re

def text_to_bit_array(text_string):
	return [x[2:] for x in map(bin, bytearray(text_string,'utf8'))]

if __name__ == '__main__':

	text = open('text.txt', 'r')
	text = ' '.join(text.readlines())
	print("Original Text: " + text)
	shift_key = 'hello world'
	cypher_text = caesar_key_encrypt(shift_key, text)
	print("Post Caesar: " + cypher_text)
	decyphered_text = caesar_key_decrypt(shift_key, cypher_text)
	print("Decyphered Caesar: " + decyphered_text)
	
	# Parameters for RSA Encryption
	p = 15299
	q = 15319
	e = 65537

	(c_msg, d, n) = rsa_encrypt(400, p, q, e)

	output = rsa_decrypt(c_msg, d, n)

	formatted_sha = ''.join('{:02x}'.format(x) for x in SHA3_256(bytearray(output)))
	
	text_binary = text_to_bit_array(text)
	polynomial = '1011'
	crc_code = crc(text_binary, polynomial)

	print("Text Binary: " + "".join(str(text_binary)))
	print("CRC: " + crc_code)

	


	





	


