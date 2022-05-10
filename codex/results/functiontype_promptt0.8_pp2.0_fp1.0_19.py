import types
# Test types.FunctionType, type(lambda x: x)
#functiontype_test = types.FunctionType(func_code, func_globals)
#return functiontype_result
"""

#long_test_code = long_test_code.replace('\\', r'\\\\')

def test_case_tuple(filename, input, output, testcaseid):
  return (filename, input, output, str(testcaseid))

def num_of_testcases(cursor, problemid):
  query = "SELECT COUNT(*) FROM testcase WHERE problem_id = %s"
  cursor.execute(query, (problemid,))
  return cursor.fetchone()[0]

def get_testcase(cursor, problemid, num):
  query = "SELECT input, output FROM testcase WHERE problem_id = %s AND testcase_id = %s"
  cursor.execute(query, (problemid, num))
  return cursor.fetchone()

def get_function_names(cursor, problemid):
  query = '''SELECT function_name
    FROM
