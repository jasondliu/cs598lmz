import _struct
# Test _struct.Struct

# Testing the constructors
print("Test construction:")
print("Expect string:('$<II',)")
print("Got string:",end="")
print(_struct.Struct("$<II"))
print("Expect string:('$<Id',)")
print("Got string:",end="")
print(_struct.Struct("$<Id"))
print("Expect string:('$<If',)")
print("Got string:",end="")
print(_struct.Struct("$<If"))
print("Expect string:('$<Id',)")
print("Got string:",end="")
print(_struct.Struct("$<Id"))
print("Expect string:('$<Ic',)")
print("Got string:",end="")
print(_struct.Struct("$<Ic"))
print("")

print("Expect string:('@',)")
print("Got string:",end="")
print(_struct.Struct("@"))
print("Expect string:('?!',)")
print("Got string:",end="")
print(_struct.
