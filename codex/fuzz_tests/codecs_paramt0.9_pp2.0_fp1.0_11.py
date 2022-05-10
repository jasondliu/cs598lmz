import codecs
codecs.register_error("gckconv", codecs.xmlcharrefreplace_errors)

WikidataItemFactory.set_items_namespaces(140, 828)
WikidataItemFactory.set_properties_namespaces(120, 828)

sp = sqlite3.connect('species.db', isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES)
sp.create_function('getRank', 1, lambda x:getRank(x))
sp.row_factory = sqlite3.Row


class DisplaySpeciesList(template_master.NegotiateTemplate):
    def __init__(self):
        super(DisplaySpeciesList, self).__init__(initial_negotiation=True, file="species_list.html")
        self.itemId = None

    def get_species_list(self):
        with sp.cursor() as s:
            if self.itemId:
                s.execute("SELECT * FROM species WHERE page_id=? UNION ALL SELECT * FROM canonicalForms WHERE page_id=?", (self.itemId, self
