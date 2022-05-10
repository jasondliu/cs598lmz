import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Python   계산기")

#이름과 전화번호 입력
user_name=input("이름을 입력하세요 : ")
user_phone = input("전화번호를 입력하세요 : ")

#입력된 이름과 전화번호 출력
print("입력된 이름은 ", user_name, "이고 전화번호는 ",user_phone, "입니다.")

#각각 문자열, 수치형 변
