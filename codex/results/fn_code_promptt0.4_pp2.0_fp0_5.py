fn = lambda: None
# Test fn.__code__
fn.__code__ = None
fn.__code__ = code
fn.__code__ = code_obj
fn.__code__ = code_obj_fn
fn.__code__ = code_obj_fn_args
fn.__code__ = code_obj_fn_args_kwargs
fn.__code__ = code_obj_fn_args_kwargs_defaults
fn.__code__ = code_obj_fn_args_kwargs_defaults_closure
fn.__code__ = code_obj_fn_args_kwargs_defaults_closure_doc
fn.__code__ = code_obj_fn_args_kwargs_defaults_closure_doc_annotations
fn.__code__ = code_obj_fn_args_kwargs_defaults_closure_doc_annotations_kwonlyargs
fn.__code__ = code_obj_fn_args_kwargs_defaults_closure_doc_annotations_kwonlyargs_kwonlydefaults
fn.__code__ = code_obj_fn_args_kwargs_defaults_closure_doc_annot
