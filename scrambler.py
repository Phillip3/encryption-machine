import re


def crc(bin_string, bin_polynomial):
	polynomial = bin_polynomial # = '1011'
	binary = bin_string
	n = len(polynomial)
	padded_binary = ''.join(binary) + ''.join(['0' for x in range(n - 1)])
	while(len(padded_binary) > n - 1):
		found_digit = re.search("1", padded_binary)
		if found_digit:
			start = found_digit.start()
			dividend = padded_binary[start:start + n]
			quotient = str(bin(int(dividend, 2) ^ int(polynomial, 2)))[2:]
			padded_binary = quotient + padded_binary[start + n:]
		else:
			print("ERROR retrieving CRC")
			return None
	return padded_binary



if __name__ == '__main__':
	expected_answer = '100'
	test_bin_string = '11010011101100'
	test_bin_polynomial = '1011'
	actual_answer = crc(test_bin_string, test_bin_polynomial)
	if str(actual_answer) == str(expected_answer):
		print('crc test passed')
	else:
		print('crc test failed')
		print('crc expected ' + expected_answer)
		print('crc received ' + actual_answer)

	





	


