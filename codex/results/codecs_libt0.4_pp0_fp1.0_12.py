import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# 기본적인 파일 입출력
# 파일 쓰기
# 파일을 쓰기모드로 열어서 파일 객체를 반환
# 파일이 없으면 새로 생성
# 파일이 있으면 덮어쓰기
# 파일 객체의 write() 메서드를 이용해서 파일에 쓸 수 있음
# 
