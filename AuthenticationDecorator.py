def auth_decorator(foo):
    def wrapper(*args):
        if user.auth:
            return foo(*args)
        else:    
            raise Exception('Ошибка входа, пожалуйста войдите в аккаунт.')
    return wrapper
