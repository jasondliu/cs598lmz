import _struct
import _lib

# int32_t  mrbc_init_class_object(struct VM *vm);
# int32_t  mrbc_init_class_array(struct VM *vm);
# int32_t  mrbc_init_class_string(struct VM *vm);
# int32_t  mrbc_init_class_range(struct VM *vm);
# int32_t  mrbc_init_class_hash(struct VM *vm);

#--------------------------------------------------------------------
# mruby/c class functions
#--------------------------------------------------------------------

def mrbc_init_class(vm, name, super):
  cls = vm.find_class(name)
  if cls:
    return cls
  if super:
    cls = mrbc_class_new(vm, name, super)
  else:
    cls = mrbc_class_new(vm, name, vm.top_class)
  return cls


def mrbc_class_new(vm, name, super):
  cls = mrbc_
