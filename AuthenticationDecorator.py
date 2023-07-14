def auth_decorator(foo):
    def wrapper(*args):
        if user.auth:
            return foo(*args)
        else:    
            raise Exception('User is not authenticated.')
    return wrapper
