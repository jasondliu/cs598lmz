import gc, weakref

from book_db_simple import (
    HumanName,
    Person,
    Book,
    Bookmark,
    rename_columns,
    get_one_or_create,
    get_or_create,
)

from base_refcount import Path, rrdump, refcounts, aa
from base_refcount import PARTIAL_REFCOUNT
from base_refcount import filter_refcounts, pprint_refcounted, pprint_refcounted_paths


################
# Create some objects
################

def make_bookdb_simple(session):
    """ Create few sample objects in "book_db_simple" database.

    @return a list created paths
    """
    paths = []
    path = None
    _, path = get_or_create(session, Person,
                    name=HumanName(given="Mickey", family="Mouse"),
                    _path=Path(many=HumanName, manyspecs=["given",]))
    paths.append(path)
    assert path.many is Path.MANY_NONE
    assert
