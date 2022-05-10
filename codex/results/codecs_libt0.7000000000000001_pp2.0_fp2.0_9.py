import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class OraclePipeline(object):
    def __init__(self):
        self.con = cx_Oracle.connect('zspider/zspider@10.230.25.67:1521/orcl')
        self.cursor = self.con.cursor()
    
    def insert(self, item):
        sql = "insert into investment_institutions(id, name, found_time, address, website, status, investor_type, investment_field, investment_stage, fund_size, introduction, reward, key_person, update_time) values (S_INVESTMENT_INSTITUTIONS.nextval, :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, sysdate)"
        self.cursor.execute(sql,
