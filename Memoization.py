def cache_dec(foo):
    db = {}
    def wrapper(*args):
        if args in db:
            return db[args]
        else:
            result = foo(*args)
            db[args] = result
            return result
    return wrapper