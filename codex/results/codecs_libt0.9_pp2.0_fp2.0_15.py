import codecs
codecs.open('./result/drinkRecipe.txt', 'r', encoding='utf-8').read()

URL='http://www.foodista.com/drink/B1FBX9HN/banana-rum-rattler'
driver=webdriver.Firefox()
driver.get(URL)
element=driver.find_element_by_xpath('//ol[@itemprop="recipeInstructions"]/li/span')
element.text


def makeListFromText(text):
    splittedText=text.replace(",","").replace(".","").replace("!","").replace("?","").split(" ")
    return splittedText

print(makeListFromText('A really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really long word'))


driver.quit()
 
from
