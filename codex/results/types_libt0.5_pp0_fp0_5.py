import types
types.new_class( 'X', (object,) )

# type(x) is 'X'
x = X()

# type(x) is 'X'
type(x)

# type(type(x)) is 'type'
type(type(x))

# type(type(type(x))) is 'type'
type(type(type(x)))

# type(type(type(type(x)))) is 'type'
type(type(type(type(x))))

# type(type(type(type(type(x))))) is 'type'
type(type(type(type(type(x)))))

# type(type(type(type(type(type(x)))))) is 'type'
type(type(type(type(type(type(x))))))

# type(type(type(type(type(type(type(x))))))) is 'type'
type(type(type(type(type(type(type(x)))))))

# type(type(type(type(type(type(type(type(x)))))))) is 'type'
