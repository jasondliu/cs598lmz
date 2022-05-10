import types
types.MethodType(lambda self: self.get_absolute_url(), Post)

# 클래스에서 정의된 메서드는 클래스 인스턴스에서만 사용할 수 있다.
# 다음 코드는 에러를 발생시킨다.
# Post.get_absolute_url()

# 클래스 인스턴스를 생성하면 클래스 인스턴스의 메서드를 호출할 수 있다.
# 클래
