import codecs
# Test codecs.register_error()
import_14254 = generate_type_inference_code_for_module(stypy.reporting.localization.Localization(__file__, 1, 0), 'codecs')

if (type(import_14254) is not StypyTypeError):

    if (import_14254 != 'pyd_module'):
        __import__(import_14254)
        sys_modules_14255 = sys.modules[import_14254]
        import_from_module(stypy.reporting.localization.Localization(__file__, 1, 0), 'codecs', sys_modules_14255.module_type_store, module_type_store, ['register_error'])
        nest_module(stypy.reporting.localization.Localization(__file__, 1, 0), __file__, sys_modules_14255, sys_modules_14255.module_type_store, module_type_store)
    else:
        from codecs import register_error

        import_from_module(stypy.reporting.localization.Localization
