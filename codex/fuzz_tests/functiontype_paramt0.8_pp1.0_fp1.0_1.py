from types import FunctionType
list(FunctionType(s.f_code,s.f_globals,s.f_name,s.f_defaults,s.f_closure)) 
# ['f_back', 'f_code', 'f_defaults', 'f_globals', 'f_locals', 'f_trace']
</code>
Hope your problem has been solved. :)

