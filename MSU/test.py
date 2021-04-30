







def create_phone_number(n):
	tn = '('
	for num in n[0:3]:
		tn+=str(num)
	else:
		tn+=') '
	for num in n[3:6]:
		tn += str(num)
	else:
		tn+='-'
	for num in n[6:]:
		tn+=str(num)
	else:
		return tn
print (create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))