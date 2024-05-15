class Product:
    def __init__(
        self, productId, productName, description, price, quantityInStock, type
    ):

        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

    def get_productId(self):
        return self.productId

    def set_productId(self, productId):
        self.productId = productId

    def get_productName(self):
        return self.productName

    def set_productName(self, productName):
        self.productName = productName

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_quantityInStock(self):
        return self.quantityInStock

    def set_quantityInStock(self, quantityInStock):
        self.quantityInStock = quantityInStock
