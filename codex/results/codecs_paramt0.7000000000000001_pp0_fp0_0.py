import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_categories_products():
    # get all subcategories
    all_categories = [c.get_descendant_categories() for c in Category.objects.all()]
    # flatten categories list
    all_categories = list(chain(*all_categories))
    return all_categories

def update_products_categories(products, dry_run=True):
    # get all categories
    all_categories = _get_categories_products()

    for product in products:
        #names = [product['Nome'], product['Nome Inglese'], product['Nome Francese']]
        names = [product['Nome Inglese']]
        print("\n\n", names)

        # search for the product
        try:
            product_obj = Product.objects.get(slug=product['Codice'].lower())
        except Product.DoesNotExist:
            print("Product not found")
            continue
        print("Found product: ", product_obj)


