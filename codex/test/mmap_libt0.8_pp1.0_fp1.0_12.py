import mmap
import os

def get_dofs_from_enum(filename, output_file, enum_name):
    """
    Get all the dofs from an enum file assuming it is in the form:
    enum EnumName
    {
        dof_name
        dof_name
        dof_name
    };
    """
    f = open(filename)
    lines = f.readlines()

    # skip the guard
    lines = lines[2:]

    # remove the ;
    lines[-1] = lines[-1].rstrip(';\r\n')

    # dofs are between curly brackets
    dof_lines = lines[1:-1]

    dofs = [x.strip() for x in dof_lines]

    # write to file
    with open(output_file, 'w') as f:
        for dof in dofs:
            f.write("{0}\n".format(dof))

