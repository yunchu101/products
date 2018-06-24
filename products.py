#read file

product =[]
with open('products.csv','r') as f:
	for line in f:
		if 'product,price' in line: #不處理資料中的這一行
			continue #跳到下一回 不會跳出迴圈
		name,price = line.strip().split(',') #strip 移除\n 隱藏換行,split 切割左右data by common
		product.append([name,price])
print(product)

#讓使用者輸入
while True:
	name = input('what did you buy? ')
	if name == 'q':
		break
	price = input('what is the price? ')
	price = int(price)
	products.append([name,price])
print(products)

#印出所有商品價格
for p in products:
	print(p[0],'的價格是',p[1])

#寫入檔案
with open ('products.csv','w',encoding='utf-8') as f:
	f.write('product,price\n')		
	for p in products:
		f.write (p[0] + ','+ str(p[1]) + '\n')
