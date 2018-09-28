#클로져
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
