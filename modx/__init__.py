def __bootstrap__():
    global __bootstrap__, __loader__, __file__
    import sys, importlib.resources as irs, importlib.util
    with irs.as_file(irs.files(__name__).joinpath('impl.py')) as __file__:
        __loader__ = None; del __bootstrap__, __loader__
        spec = importlib.util.spec_from_file_location(__name__,__file__)
        mod = importlib.util.module_from_spec(spec)
        print('my_function' in dir(globals()))
        spec.loader.exec_module(mod)
        print('my_function' in dir(mod))
        print('my_function' in dir(globals()))
__bootstrap__()
