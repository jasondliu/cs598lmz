import threading
threading.stack_size(1024*1024*8)


# Cặp đầu vào / đầu ra
# Dữ liệu đầu vào của mạng nơ ron là giá
# Dữ liệu đầu ra của mạng nơ ron là giá biến động tương lai
window = 10
input = 1
output = 1

# Khai báo các hằng số của mô hình
input_size = input * window
hidden_size = 128
output_size = output * window

# Khởi tạo dữ liệu huấn luyện
def get_data():
    train_data = pd.read_csv('/home/
