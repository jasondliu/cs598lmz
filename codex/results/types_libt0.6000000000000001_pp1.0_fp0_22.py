import types
types.MethodType(create_random_arr, np)

np.random.rand(4)
np.random.rand(4, 5)

np.random.randint(5)  # 0~4 사이의 정수
np.random.randint(5, size=5)  # 0~4 사이의 정수 5개
np.random.randint(5, size=(2, 3))  # 0~4 사이의 정수 2행 3열

np.random.randint(5, 10)  # 5~9 사이의 정수
np.random.randint(5, 10, size=5)  # 5~9 사이의 정수 5개
np.random.randint(5, 10, size=(2, 3))  # 5~9 사이의 정수 2행 3열

np.random.random() 
