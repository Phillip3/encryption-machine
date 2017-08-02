from SHA3 import *

alphabet = list('abcdefghijklmnopqrstuvwxyz')

def caesar_key_encrypt(shift_key, text):
	key_numbers = [alphabet.index(x) for x in list(shift_key.lower()) if x in alphabet]
	text_in_numbers = [alphabet.index(x) for x in list(text.lower()) if x in alphabet]
	shifted_text_numbers = [x + key_numbers[ind % len(key_numbers)] for ind, x in enumerate(text_in_numbers)]
	encrypted_text = ''.join([alphabet[x - 26] for x in shifted_text_numbers])
	return encrypted_text

def caesar_key_decrypt(shift_key, encrypted_text):
	shift_key_numbers = [-alphabet.index(x) for x in list(shift_key.lower()) if x in alphabet]
	return caesar_key_encrypt(''.join([alphabet[x] for x in shift_key_numbers]), encrypted_text)

def spread_power(power, threshold):
	'''recursively creates a list of integers
	that add up to the given integer 'power' where all are below
	the 'threshold' '''
	if power < threshold:
		return [power]

	if power % 2:
		return spread_power(power/2+1, threshold) + \
		spread_power(power/2, threshold)
	else:
		return spread_power(power/2, threshold) + \
		spread_power(power/2, threshold)


def fast_mod_exp(a, b, n):
    '''((a^b)mod(n))'''
    powers_list = spread_power(b, 30)
    # print(powers_list)
    mult_list = [a**p%n for p in powers_list]
    result = 1
    for mult in mult_list:
    	result = (mult*result)%n
    return result

def rsa_decrypt(c, d, n):
	print('Decrypting...')
	# decrypted = (c**d)%n
	# making c**d faster
	print('taking %i^%imod%i'%(c, d, n))
	decrypted = fast_mod_exp(c, d, n)

	print('original = %i'%decrypted)
	return decrypted

def rsa_encrypt(m, p, q, e):
	'''m is the message in the form of a number less than p*q,
	p and q are both prime integers that are sufficiently large
	and e is some other prime that has somethign to do with
	the totient. Please read up on that before you use this fxn.'''

	n = p * q
	totient = (p - 1) * (q - 1)

	# the inverse of e mod totient is d.
	# calculating the modular inverse

	(dividend, divisor) = (totient, e)
	p0 = 0
	p1 = 1

	while True:
		(q, r) = divmod(dividend, divisor)
		p2 = (p0 - (p1 * q)) % totient
		dividend = divisor
		divisor = r
		p0 = p1
		p1 = p2
		if r == 0 or q == 0:
			break
	# p0 is the modular inverse
	d = p0
	print('public key is (%i, %i)'%(e, n))
	print('private key is (%i, %i)'%(d, n))
	m = 400
	print('Encrypting %i'%m)
	encrypted_message = fast_mod_exp(m, e, n) #(m**e)%n
	print('Encrypted message: %i'%encrypted_message)
	return (encrypted_message, d, n)

if __name__ == '__main__':
	p = 15299
	q = 15319

	e = 65537
	input_text = 400
	(c_msg, d, n) = rsa_encrypt(input_text, p, q, e)

	output = rsa_decrypt(c_msg, d, n)
	if input_text == output:
		print('rsa test passed')
	else:
		print('rsa test failed')
		print('rsa test expected ' + input_text)
		print('rsa test received ' + output)



	





	


