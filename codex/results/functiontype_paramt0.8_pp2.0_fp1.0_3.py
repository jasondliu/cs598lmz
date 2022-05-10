from types import FunctionType
list(FunctionType(lambda:0,{'+':lambda a,b:a+b},None,None,"<lambda>",0,0).__code__.co_names)

Your code can also use its own builtins, as long as you make sure they also get passed in as an argument to FunctionType.

[
    amd_lang_abstract_syntax_tree,
    amd_lang_abstract_syntax_tree_node,
    amd_lang_abstract_syntax_tree_edge,
    amd_lang_arithmetic_operators,
    amd_lang_builtin_funcs,
    amd_lang_code_generator,
    amd_lang_core_memory,
    amd_lang_core_memory_cell,
    amd_lang_fibonacci,
    amd_lang_graph_``,
    amd_lang_graph_node,
    amd_lang_graphics,
    amd_lang_graphics_``,
    amd_lang_graphics_color,
    amd_lang_graphics_color_``,
    amd_lang_g
