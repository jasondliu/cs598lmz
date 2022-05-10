fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Top-level code object
# Is active when the execution of the module code is started
# It is executed when the module is loaded as a script
# It is also executed when the module is imported
# It is executed when the module is loaded as a script
# It is not executed when the module is imported
# It is executed once

# Module code object
# It is executed when the module is imported


# Function code object
# It is executed when the function is called
