from types import FunctionType
list(FunctionType(op.__call__, {}).__closure__)

# op.__call__.__closure__

# op_closure = [x.cell_contents for x in op.__call__.__closure__]
# op_closure[5].__class__

# 0:  <module 'tensorflow._api.v1.compat.v2.config' from '/Users/marcotcr/miniconda3/envs/recsys/lib/python3.7/site-packages/tensorflow_core/_api/v1/compat/v2/config/__init__.py'>
# 1:  '_internal_api'
# 2:  <module 'tensorflow._api.v1.compat.v2.logging' from '/Users/marcotcr/miniconda3/envs/recsys/lib/python3.7/site-packages/tensorflow_core/_api/v1/compat/v2/logging/__init__.py'>
# 3:  '_internal_api'
# 4:  <
