from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# _struct.Struct.pack
# _struct.Struct.unpack
# _struct.Struct.iter_unpack

# _pickle.Pickler.dump
# _pickle.Pickler.clear_memo
# _pickle.Pickler.getvalue

# _pickle.Unpickler.load
# _pickle.Unpickler.noload
# _pickle.Unpickler.find_class
# _pickle.Unpickler.persistent_load

# _pickle.Pickler.dispatch
# _pickle.Unpickler.dispatch
# _pickle.Pickler.save
# _pickle.Unpickler.load_reduce
# _pickle.Unpickler.load_build

# _pickle.Pickler.save_pers
# _pickle.Pickler.save_reduce
# _pickle.Pickler.save_inst
# _pickle.Pickler.save_global

# _pickle.Unpickler.
