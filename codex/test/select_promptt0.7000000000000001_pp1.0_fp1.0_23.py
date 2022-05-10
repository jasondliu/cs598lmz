import select
# Test select.select()

print('*******select.select()*******')

# 接受输入并返回第一个

def get_key():
	i, _, _ = select.select([sys.stdin], [], [], 0.1)
	
	if i:
		print('stdin:', sys.stdin.readline().strip())
		
	else:
		print('no input')

# 输入

while(1):
	get_key()
	
# 按q退出

# ********select.select()********
# no input
# no input
# no input
# no input
# no input
# no input
# no input
# no input
# no input
# no input
# no input
# no input
