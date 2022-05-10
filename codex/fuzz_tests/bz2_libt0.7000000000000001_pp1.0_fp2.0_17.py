import bz2
bz2.BZ2File.MAX_WBITS = 33

# Get the names of the input parameters
def get_parm_names(parm_file):
    # Read the first line of the parm file
    line = parm_file.readline()

    # This should be the parameter names
    names = line.split(',')

    # Remove the first column name
    names = names[1:]

    # Convert from string to unicode
    names = [unicode(name, 'utf-8') for name in names]

    return names


# Get the values of the input parameters
def get_parm_values(parm_file):
    # Read the next line of the parm file
    line = parm_file.readline()

    # This should be the parameter values
    values = line.split(',')

    # Remove the first column value
    values = values[1:]

    return values


# Get the names of the output parameters
def get_output_names(output_file):
    # Read the first line of the output file
    line = output_
