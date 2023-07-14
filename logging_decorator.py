def log_decorator(foo):
    import logging
    print(foo.__name__)
    logging.basicConfig(filename='logs.log', level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kwargs {kwargs}")
        return foo(*args, **kwargs)
    return wrapper

        