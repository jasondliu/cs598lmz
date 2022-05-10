import types
types.CodeType(123, 123, 123, 123, 123, 123, 123, 0, 123, 123, 123)

#:: ExpectedOutput(assert.failed:assertion_error)
types.CodeType(123, 123, 123, 123, 123, 123, 123, 0, 123, 123, "a")

#:: ExpectedOutput(assert.failed:assertion_error)
types.CodeType(123, 123, 123, 123, 123, 123, 123, 0, 123, 123, 123, 123)

#:: ExpectedOutput(assert.failed:assertion_error)
types.CodeType("a", 123, 123, 123, 123, 123, 123, 0, 123, 123, 123)

#:: ExpectedOutput(assert.failed:assertion_error)
types.CodeType("a", 123, 123, 123, 123, 123, 123, 0, 123, 123, 123, 123)

#:: ExpectedOutput(assert.failed:assertion_error)
