import select_clause
import where_clause
import group_clause
import order_clause
import limits_clause
import subquery
import name_resolution
import function_builder
import function
import syntax_tree
import aggregate
import union


def test_select_clauses(conn):
    query = select_clause.Query(conn, 'SELECT 1')
    assert str(query) == 'SELECT 1'
    query = select_clause.Query(conn, 'SELECT 1 FROM a')
    assert str(query) == 'SELECT 1 FROM a'
    query = select_clause.Query(conn, 'SELECT 1, 2')
    assert str(query) == 'SELECT 1, 2'
    query = select_clause.Query(conn, 'SELECT 1, 2 FROM a')
    assert str(query) == 'SELECT 1, 2 FROM a'
    query = select_clause.Query(conn, 'SELECT 1, 2 FROM a, b')
    assert str(query) == 'SELECT 1, 2 FROM a, b'
    query = select_clause.Query(conn, '
