import codecs
codecs.register_error("strict_json", strict_json)
with codecs.open('./data/m_recipe.json', 'r', 'utf-8', errors='strict_json') as f:
    recipe = json.load(f)
with codecs.open('data/m_ingredient.json', 'r', 'utf-8', errors='strict_json') as f:
    ingredient = json.load(f)
with codecs.open('data/m_material.csv', 'r', 'utf-8', errors='strict_json') as f:
    material = pd.read_csv(f)
# recipe_dataとpredict_dataを紐づけ
recipe_data_id = pd.merge(recipe_data, 
                          recipe, 
                          left_on='recipe_id', right_on='recipe_id', 
                          how='left')

recipe_data_id['density'] = recipe_data_id['density'].fillna(0)

# レシピデー
