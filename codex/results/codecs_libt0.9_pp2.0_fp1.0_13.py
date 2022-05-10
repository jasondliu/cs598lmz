import codecs
codecs.open('recipes.txt',mode='r',encoding='utf-8',errors='strict')

# Read the entire file at once
with open('recipes.json') as fin:
    text = fin.read()

# Read the file one line at a time
with open('recipes.json') as fin:
    for line in fin:
        pass # do something with the line

def parse_ingredients(ingredients_str):
    ingredients = []
    for line in ingredients_str.split('\n'):
        if not line:
            continue
        amount, unit, name = get_amount(line)
        # Some measurements are listed without units
        if amount and not unit: 
            unit = infer_unit(name)
        ingredients.append(Ingredient(
            name=name,
            quantity=amount,
            measurement=unit)
        )
    return ingredients

def infer_unit(name):
    units = {'eggs': 'whole'}
    return units.get(name)

for recipe in recipes:
    for ingredient in
