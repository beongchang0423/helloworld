
# 네임스페이스
함수에서 전역 변수의 값을 얻어서 바꾸려 하면 에러가 발생한다.
```python
animal = 'fruitbat'
 def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)
 change_and_print_global()
```
```
Traceback (most recent call last):
  File "d:\_Nest\code\introducing_python\ch01\ex_1_2.py", line 8, in <module>
    change_and_print_global()
  File "d:\_Nest\code\introducing_python\ch01\ex_1_2.py", line 4, in change_and_print_global
    print('inside change_and_print_global:', animal)
UnboundLocalError: local variable 'animal' referenced before assignment
```
 다음은 함수 내의 지역 변수이다.
```python
def change_local():
    animal = 'wombat2'
    print('inside change_local:', animal, id(animal))
 change_local()
```
 함수 내에서 지역 변수가 아닌 전역 변수를 접근하기 위해 global 키워드를 사용해서 전역 변수의 접근을 명시해야 한다.
함수 안에 global 키워드를 사용하지 않으면 로컬 네임스페이스를 사용한다.
```
animal = 'fruitbat'
 def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)
 print(animal)
change_and_print_global()
print(animal)
```
```
fruitbat
inside change_and_print_global: wombat
wombat
```
 ## 네임스페이스 함수
- locals(): 로컬 네임스페이스의 내용이 담긴 딕셔너리를 반환한다.
- globals(): 글로벌 네임스페이스의 내용이 담긴 딕셔너리를 반환한다.
 ```python
animal = 'fruitbat'
 def change_local():
    animal = 'wombat'   # 지역변수
    print('locals:', locals())
 print(animal)
change_local()
print('globals', globals()) # 보여주기 위한 작은 출력 포멧
print(animal)
```
 ## _ 와 __
__ 로 시작하는 변수는 시스템 예약으로 사용하면 안된다.
 ```python
def amazing():
    '''this is the amazing function.
    Want to see it again?'''
    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)
amazing()
