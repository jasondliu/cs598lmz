import threading
threading.stack_size(102400)

def tf_idf(file_path):
    count_all_words = {}  # 全局的字典，key:单词，value:出现的次数
    global_set = set()  # 全局的集合，存放所有的单词，去重
    idf_dict = {}  # 全局的字典，key:单词，value:idf值
    tf_idf_dict = {}  # 全局的字典，key:单词，value:tf-idf值

    # 计算每个单词出现的次数
