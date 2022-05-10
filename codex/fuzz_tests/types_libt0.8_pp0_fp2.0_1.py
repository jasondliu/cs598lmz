import types
types.ClassType
type(types.ClassType)
type is types.ClassType

# 상속
# list -> stack
# 직접 상속은 유지보수가 어렵다
class Stack(list):
    def push(self, a):
        self.append(a)

# 상속은 조상을 통해서 부모를 호출하지 않는 방법 -> 상속 규칙에 벗어나서 재정의 가능
# 부모를 호출하려면 __super__ 객체를 사용한다 -> 클래
