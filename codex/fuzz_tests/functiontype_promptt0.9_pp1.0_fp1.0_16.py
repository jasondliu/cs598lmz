import types
# Test types.FunctionType
if False:
    from typing import Dict, List, Tuple, Union, Optional

def get_search_url(text): pass

def get_recipe_links(search_url): pass

def get_recipe_nutrients(recipe_links): pass
def get_recipe_ingredients(recipe_links): pass
def get_recipe_babyname(recipe_links): pass

def create_pandas_dataframe(recipe_links): pass
def create_excel_file(recipe_gdf): pass
    
def main():
    search_url = get_search_url(SEARCH_REQUEST)
    recipe_links = get_recipe_links(search_url)
    recipe_gdf = create_pandas_dataframe(recipe_links)
    create_excel_file(recipe_gdf)
if __name__ == "__main__":
    main()
