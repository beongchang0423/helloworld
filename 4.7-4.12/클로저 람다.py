#클로져
def outer_print(msg):
  def inner_print():
    print('hello %s'%msg)
  return inner_print
printer = outer_print('Hi')
printer()

#익명함수 : lambda()
def edit_story(words,func):
  for word in words:
    print(func(word))
stairs = ['thub','meo','hiss']
def enliven(word):
  return word. capitalize() + '!'

edit_story(stairs, enliven)
edit_story_2(stairs, lambda word: word.capitalize() + '!')

sum = lambda a, b: a+b
sum(3,4)
def sum(a,b):
    return a+b
sum(3,4)
