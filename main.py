from dao.OrderProcessor import OrderProcessor
from entity.Electronics import Electronics
from entity.User import User
from entity.Clothing import Clothing
from entity.Product import Product
from exception.invalid_user_exception import InvalidUserException
from exception.user_not_found_excception import UserNotFoundException

print("Welcome to Order app..!!")


def main():
    order_processor = OrderProcessor()
    while True:
        print(
            """Helloo..
            1. Create User
            2. Create Product
            3. Cancel Order
            4. Get all Products
            5. Get Order By user
            6. Exit
              """
        )

        choice = int(input("Enter your choice: "))
        if choice == 1:
            user_id = int(input("Enter a new use id: "))
            username = input("Enter the user name : ")
            password = input("pls give a password: ")
            role = input("Enter role (Admin/User): ")
            order_processor.create_user(user_id, username, password, role)
            print("User created successfully.")

        elif choice == 2:
            try:
                product_id = int(input("Enter a new product id to create: "))
                product_name = input("Enter its product name: ")
                description = input("Give a valid  description: ")
                price = float(input("Enter amt for the product: "))
                quantity_in_stock = int(input("Enter quantity available: "))
                product_type = input("Enter type (Electronics/Clothing): ")
                order_processor.create_product(
                    product_id,
                    product_name,
                    description,
                    price,
                    quantity_in_stock,
                    product_type,
                )

                print("Product created successfully.")
            except InvalidUserException as e:
                print(e)

        elif choice == 3:
            user_id = int(input("Enter your user ID: "))
            order_id = int(input("Enter your order ID: "))

            try:
                order_processor.cancel_order(user_id, order_id)
                print("Order canceled successfully.")
            except UserNotFoundException as e:
                print(e)

        elif choice == 4:
            totals = order_processor.get_all_products()
            for total in totals:
                print(total)

        elif choice == 5:
            usr_name = input("Enter username: ")

            try:
                orders = order_processor.get_orders_by_user(usr_name)
                for order in orders:
                    print(order)
            except UserNotFoundException as e:
                print(e)

        elif choice == 6:
            print("Exit")
            break


if __name__ == "__main__":
    print("Hello welcome to orders app..")
    print("Lets enter!!")
    main()
