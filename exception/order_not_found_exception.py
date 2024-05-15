class OrderNotFoundException(Exception):
    def _init_(self, message):
        super()._init_(message)
