import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)
 
# Open database connection
connection = pymysql.connect(host='localhost',
                             user='',
                             password='',
                             db='luminous',
                             charset='utf8')

class AlexaAbstract:
    def __init__(self, slotVar, sqlQuery, sqlQueryRestriction):
        self.slotVar = slotVar
        self.sqlQuery = sqlQuery
        self.sqlQueryRestriction = sqlQueryRestriction
        
    def hasSlotVar(self):
        return self.slotVar and type(self.slotVar) == str
        
    def getSlotVar(self):
        return self.slotVar
    
    def getQuery(self, fullQuery):
        if self.hasSlotVar():
            return self.sqlQuery.replace('%s', self.slotVar)
        else:
            return self.sqlQuery
        
    def getFullQuery(self, fullQuery):
        if self.hasSlotVar
