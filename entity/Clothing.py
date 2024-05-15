from entity.Product import Product


class Clothing(Product):
    def _init_(
        self,
        product_id,
        product_name,
        description,
        price,
        quantity_in_stock,
        product_type,
        size,
        color,
    ):
        super()._init_(
            product_id,
            product_name,
            description,
            price,
            quantity_in_stock,
            product_type,
        )
        self.size = size
        self.color = color
