import os # operating system 請問政府大人 載入模組

def read_file(filename):
	products =[] #不管有沒有找到檔案, 都要產生空清單
	with open(filename,'r') as f: #read file
		for line in f:
			if 'product,price' in line: #不處理資料中的這一行
				continue #跳到下一回 不會跳出迴圈
			name,price = line.strip().split(',') #strip 移除\n 隱藏換行,split 切割左右data by common
			products.append([name,price])
	return products	
#讓使用者輸入
def user_input(products):
	while True:
		name = input('what did you buy? ')
		if name == 'q':
			break
		price = input('what is the price? ')
		price = int(price)
		products.append([name,price])
	print(products)
	return products

#印出所有商品價格
def print_product(products):
	for p in products:
		print(p[0],'的價格是',p[1])
#寫入檔案
def write_file(filename, products):
	with open (filename,'w',encoding='utf-8') as f:
		f.write('product,price\n')		
		for p in products:
			f.write (p[0] + ','+ str(p[1]) + '\n')
def main():
	if os.path.isfile('products.csv'): #檢察檔案是否存在  #若不在同一個資料夾，需給完整path
		print('yeah! file is there')
		products = read_file('products.csv')
	else:
		print('找不到檔案！')
	products = user_input(products)
	print_product(products)
	write_file('products.csv',products)

main()
