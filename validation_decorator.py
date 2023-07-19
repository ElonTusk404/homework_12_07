def check(**kwargs):
    def dec(foo):
        def wrapper(*args, **kwargs):
            for name, type in args.items():
                if not isinstance(kwargs[name], type):
                    raise TypeError(f'{name} должен иметь тип: {type}')
            return foo(*args, **kwargs)
        return wrapper
    return dec
