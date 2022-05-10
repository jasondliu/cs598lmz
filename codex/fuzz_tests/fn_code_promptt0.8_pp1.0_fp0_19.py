fn = lambda: None
# Test fn.__code__.co_argcount since we can't see __code__ on Python 3
# lambda x: None has __code__.co_argcount = 1, lambda has __code__.co_argcount = 0
assert fn.__code__.co_argcount == 0

import os
import platform

def is_win():
    return platform.system().find('win') >= 0

def check_shell_vars(shell,
                     env_var,
                     env_val,
                     env_val2,
                     env_val3,
                     str1,
                     str2,
                     target_dir):
    # Check correct environment variables are set
    env_var1 = shell.get_env_var(env_var)
    assert env_var1 == env_val or env_var1 == env_val3, \
        "Incorrect value, expected '%s' or '%s' got '%s'" % (env_val, env_val3, env_var1)

    # Check correct environment variables are set
    env_var2 = shell.get_env_var(env
