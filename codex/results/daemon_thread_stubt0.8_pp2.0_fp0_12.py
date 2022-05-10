import sys, threading

def run():
    # print(sys.argv)    # ex. ['D:\pythonworkspace\GitHub\Python\selenium\ex.py', '-v', '--browser=chrome']
    # print(sys.argv[1:])    # ex. ['-v', '--browser=chrome']
    # parser.add_option의 인자를 나누기 위해서 생성한 리스트
    option_list = ["--browser", "--address", "--log-level"]
    argv = []

    # 파싱한 인자를 다시 합쳐서 새로운 리스트에 저장
    for x in sys.argv:
        for temp in option_list:
            # 파싱한 인자와 option_list
