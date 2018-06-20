products = []
while True:
	name = input('what did you buy? ')
	if name == 'q':
		break
	price = input('what is the price? ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
	print(p)
print(products)
print(products[0][0])
