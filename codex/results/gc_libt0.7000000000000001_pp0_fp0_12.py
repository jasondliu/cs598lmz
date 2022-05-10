import gc, weakref, ctypes

import pytest

from zope.interface.verify import verifyObject

class TestDummyResource:

    def test_verify_interface(self):
        from zope.interface.verify import verifyObject
        from txdav.who.idirectory import IDirectoryResource
        from txdav.who.directory_record import DirectoryRecord
        verifyObject(IDirectoryResource, DirectoryRecord(None, None, None, None,
                                                         None, None))

    def test_recordType(self):
        from txdav.who.directory_record import DirectoryRecord
        record = DirectoryRecord(None, None, None, None, None, None)
        assert record.recordType() == record.service.recordType


    def test_shortNames(self):
        from txdav.who.directory_record import DirectoryRecord
        record = DirectoryRecord(None, None, None, None, None, None)
        assert record.shortNames == []


    def test_fullName(self):
        from txdav.who.directory_record import DirectoryRecord

