products = []
while True:
	name = input('what did you buy? ')
	if name == 'q':
		break
	price = input('what is the price? ')
	price = int(price)
	products.append([name,price])
print(products)
print(products[0][0])

for p in products:
	print(p[0],'的價格是',p[1])

with open ('products.csv','w',encoding='utf-8') as f:
	f.write('product,price\n')		
	for p in products:
		f.write (p[0] + ','+ str(p[1]) + '\n')
