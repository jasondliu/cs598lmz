fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)(co_argcount=0)
fn.__code__.co_freevars = ()
gi.gi_frame = fn.__code__.co_varnames = ()
gi.gi_running = False
gi.gi_frame.f_locals = {}
gi.gi_frame.f_globals = {}

__all__ = ("dummy_exec", "dummy_eval", "dummy_execfile", "dummy_compile",
           "dummy_compile_restricted", "dummy_compile_command",
           "dummy_run_code", "dummy_run_compiled_code",
           "dummy_run_restricted_code", "dummy_run_restricted_compiled_code",
           "dummy_run_command", "dummy_run_restricted_command",
           "dummy_run_module", "dummy_run_restricted_module",
           "dummy_run_module_as_main", "dummy_run_restricted_module_as_
