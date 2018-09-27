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
