#위치인자
def menu(wine, entree, dessert):
  return {'wine': wine, 'entree': entree, 'dessert' : dessert}
menu('chardonnay','chicken','cake')

menu('beef','bagel','bordeaux')
#키워드인자
menu(entree='beef',dessert='bagel',wine = 'bordeaux')

menu('frontenac',dessert ='flan', entree= 'fish')
#기본 매개변수값 지정하기
def menu_2(wine,entree,dessert='pudding'):
  return {'wine': wine, 'entree': entree, 'dessert' : dessert}

menu_2('chardonnay','chicken')

menu_2('dunkelfelder','duck','doughnut')
#위치인자 모으기:*
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
result = sum_many(1,2,3,4,)
print(result)
#키워드 인자 모으기:**
def function(**kwargs):
  print(kwargs)
function(a = 1)
function(name = 'foo',age = 3)
#docstring
def echo(anything):
	'echo returns its input argument'	
	return anything
#docstring출력
help(echo) #또는
print(echo.__doc__)
