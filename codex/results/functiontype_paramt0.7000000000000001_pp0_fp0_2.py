from types import FunctionType
list(FunctionType(lambda a:a + 1,
                  {},
                  'f',
                  (object,),
                  None)
     .__dict__)

# <<Script list(FunctionType(lambda a:a + 1,
# .....              {},
# .....              'f',
# .....              (object,),
# .....              None)
# .....      .__dict__)
# {}
# ---
# >>END
