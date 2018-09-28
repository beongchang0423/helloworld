#예외 처리하기 예시
try:
    4 / 0
except ZeroDivisionError as e:
    print(e) # dicision by zero 출력
    
short_list = [1,2,3]
position = 5
try:
  short_list[position]
except:
  print('Need a position between 0 and', len(short_list)-1, 'but got',position)
  #예외 만들기
class MyError(Exception):
    pass
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)  
say_nick("천사")
say_nick("바보")
