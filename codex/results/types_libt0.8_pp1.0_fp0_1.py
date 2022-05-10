import types
types.MemberType.MEMBER
import json


class BuildEvent:
    def __init__(self, event_type, member_type, member, version, db_status, db_last_modified, db_id,
                 event_id, timestamp, status, message, _id, collection, db_name, db_description, db_version):
        self.event_type = event_type
        self.member_type = member_type
        self.member = member
        self.version = version
        self.db_status = db_status
        self.db_last_modified = db_last_modified
        self.db_id = db_id
        self.event_id = event_id
        self.timestamp = timestamp
        self.status = status
        self.message = message
        self._id = _id
        self.collection = collection
        self.db_name = db_name
        self.db_description = db_description
        self.db_version = db_version


def get_dict(build_event):
    d = {}
    try:
        d
