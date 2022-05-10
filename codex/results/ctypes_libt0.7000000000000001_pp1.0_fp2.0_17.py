import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\Users\tesla\Downloads\66.jpg', 0)

'''

'''
for i in range(1, 10):
    with open(r'C:\Users\tesla\Documents\Python Scripts\PythonStudy\ttt\{}.txt'.format(i), 'w') as f:
        f.write(str(random.randrange(1, 10)))
        f.write("\n")


with open(r'C:\Users\tesla\Documents\Python Scripts\PythonStudy\ttt\t.txt', 'w') as f:
    for i in range(1, 10):
        f.write(str(random.randrange(1, 10)))
        f.write("\n")
'''

#%%
ttt = []
for i in range(1, 10):
    with open(r'C:\Users\tesla\Documents\Python Scripts\PythonStudy\ttt\{}.txt'.format(i), 'r') as f:
        t
