#앞에서 배웠던 함수들은 pyton3에 내장되어있는 함수였고
# def를 이용하는 것은 원하는 함수를 직접 만드는 것이다.

#예제1. (*def = definition의 줄임말)
def sum(a,b): #여기 a,b는 매개변수
  return a + b
a = 3
b = 4
print(sum(a,b)) # 여기a,b는 인수

# 매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고 
# 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.


def make_a_sound():   #매개변수 x인 함수정의 def=definition의 줄임말
  print('quack')
make_a_sound()

def echo(something): #something이라는 변수를 입력받는 함수정의
  return something + '' + something
echo('abcdefg')
