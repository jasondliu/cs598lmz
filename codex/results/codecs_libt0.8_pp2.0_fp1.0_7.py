import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from models import connection, Play, Play_Fossil, Play_Fossil_Node, Play_Fossil_Edge
session = connection.create_scoped_session()

class Fossils:
    def __init__(self):
        self.m_session = session

    def getFossilList(self, fossil_list):
        if fossil_list is None:
            return ''
        fossil_list = fossil_list.split(',')
        fossil_obj_list = []
        for fossil_id in fossil_list:
            fossil_obj = session.query(Play_Fossil).filter(Play_Fossil.id == fossil_id).first()
            if fossil_obj is not None:
                fossil_obj_list.append(fossil_obj.to_json())
        return fossil_obj_list

    def getFossilNodeList(self, fossil_id):
        fossil_node_list = session.query(Play_
