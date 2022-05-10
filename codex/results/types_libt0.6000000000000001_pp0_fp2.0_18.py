import types
types.ClassType = type

class AbstractDataSource(object):
    """
    A data source is a wrapper around a file-like object that provides
    a number of methods for reading data in different formats.

    The interface is as follows:

    * get_next_value()
    * get_next_values(num_values=1)
    * get_next_line()
    * get_next_lines(num_lines=1)
    * get_lines(start_offset, num_lines)
    * get_value(offset)
    * get_values(start_offset, num_values)
    * get_value_at_line(line_num)
    * get_value_at_lines(line_nums)
    * get_values_at_line(line_num, num_values)
    * get_values_at_lines(line_nums, num_values)
    * get_all_values()
    * get_all_lines()
    * get_all_values_at_line(line_num)
    * get_all_values_at
