products = []
while True:
	name = input('what did you buy? ')
	if name == 'q':
		break
	price = input('what is the price? ')
	products.append('name','price')
print(products)
print(products[0][0])
