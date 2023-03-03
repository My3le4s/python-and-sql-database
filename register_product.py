from main import Product

try:
    product_price = input("Enter price: \n")
    product_quantity = input("Enter quantity: \n")
    product_description = input("Enter description: \n")
    product_color = input("Enter color: \n")


    Product.create_table(Product_price=product_price, Product_quantity=product_quantity, Product_description=product_description, Product_color=product_color)
    print("Product Created Successfully")
except:
    print("Failed to Create Products")