import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 실행 구문
app.run(host='0.0.0.0', port=5000, debug=True)

# 윈도우 환경에서 pip install gunicorn 로 설치 후
# gunicorn -w 4 -b 0.0.0.0:5000 app:app 로 실행
# 이때 -w는 작업자 쓰레드 개수, -b는 서버 주소와 포트 번호를 지정
# 표준 배포판의 경우 아래
