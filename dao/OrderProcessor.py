from dao.IOrderManagementRepository import IOrderManagementRepository
from entity import Electronics, Clothing
from entity.Product import Product
from exception import (
    invalid_user_exception,
    user_not_found_excception,
)
from exception.order_not_found_exception import OrderNotFoundException
from util.DBConn import DBConnection


class OrderProcessor(DBConnection, IOrderManagementRepository):
    def create_order(self, user, products):

        self.cursor.execute("SELECT * FROM Users WHERE userId=?", (user.user_id,))
        user_data = self.cursor.fetchone()
        if not user_data:
            self.cursor.execute(
                "INSERT INTO Users  VALUES (?,?,?,?)",
                (user.user_id, user.username, user.password, user.role),
            )
            self.conn.commit()

        self.cursor.execute("INSERT INTO Orders VALUES ?", (user.user_id,))
        order_id = self.cursor.lastrowid

        for product in products:
            self.cursor.execute(
                "INSERT INTO OrderDetails (orderId, productId) VALUES (?, ?)",
                (order_id, product.product_id),
            )
        self.conn.commit()

    def cancel_order(self, user_id, order_id):

        self.cursor.execute(
            "SELECT * FROM Orders WHERE orderId=? AND userId=?", (order_id, user_id)
        )
        order_data = self.cursor.fetchone()
        if not order_data:
            raise OrderNotFoundException("Order not found")
        self.cursor.execute("DELETE FROM Orders WHERE orderId=?", (order_id,))

    def create_product(
        self,
        product_id,
        product_name,
        description,
        price,
        quantity_in_stock,
        product_type,
    ):

        self.cursor.execute(
            "INSERT INTO Product VALUES (?,?,?,?,?,?)",
            (
                product_id,
                product_name,
                description,
                price,
                quantity_in_stock,
                product_type,
            ),
        )
        if product_type.lower() != "admin":
            raise invalid_user_exception.InvalidUserException(
                "Only admins can create products"
            )

    def create_user(self, user_id, username, password, role):

        self.cursor.execute(
            "INSERT INTO Users VALUES (?,?,?,?)",
            (user_id, username, password, role),
        )

    def get_all_products(self):

        self.cursor.execute("SELECT * FROM Product")
        Product = self.cursor.fetchall()
        return Product

    def get_orders_by_user(self, usr_name):

        self.cursor.execute("SELECT * FROM Users WHERE username=?", (usr_name))
        user_data = self.cursor.fetchall()
        if not user_data:
            raise user_not_found_excception.UserNotFoundException("User not found")

        return user_data
