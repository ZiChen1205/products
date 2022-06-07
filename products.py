import os
#讀取檔案
def read_file(filename):
	products = []
	with open(filename,'r', encoding = 'utf-8') as f:
		for line in f:
			if '名稱,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])	
	return products

def user_input(products):
	#讓使用者輸入
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0],'的價格是',p[1])

# 寫入檔案
def write_file(filename,products):
	with open(filename,'w',encoding = 'utf-8') as f:
		f.write('名稱,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #確認檔案是否存在
		print('找到了!')
		products = read_file(filename)
	else:
		print('找不到該檔案!')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
