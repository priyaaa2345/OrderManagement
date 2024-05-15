from entity.Product import Product


class Electronics(Product):
    def _init_(
        self,
        product_id,
        product_name,
        description,
        price,
        quantity_in_stock,
        product_type,
        brand,
        warranty_period,
    ):
        super()._init_(
            product_id,
            product_name,
            description,
            price,
            quantity_in_stock,
            product_type,
        )
        self.brand = brand
        self.warranty_period = warranty_period
