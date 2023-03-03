
from main import Product

products = Product.select()
for product in products:
    print(Product.Product_price, Product.Product_quantity, Product.Product_description, Product.Product_color)