import threading
threading.stack_size(2*1024*1024)

# 쓰레드 정보 확인
thread = threading.current_thread()
print("쓰레드 이름:", thread.name)
print("쓰레드 번호:", thread.ident)
print("쓰레드 종료 여부:", thread.is_alive())
print("쓰레드 그룹:", thread.daemon)
print("쓰레드 레벨:", thread.getName())

# 쓰레드 만들기
def test_thread():
  print("쓰레드 시작")
  for i in range(5):
    print("쓰레드 진행..")

