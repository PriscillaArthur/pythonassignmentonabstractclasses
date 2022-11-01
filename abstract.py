from abc import ABC,abstractmethod

class Product:
    Product_name="Buildryt"
    Product_id=23
    product_image=''
    product_cost=100
    product_type=""

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self,Product):
        pass
    @abstractmethod
    def edit_product(self,Product_id):
        pass
    @abstractmethod
    def get_product_by_id(self,Product_id):
        pass
    @abstractmethod
    def get_all_products(self):
        pass
    @abstractmethod
    def upload_product_image(self,Product_id,Product_image):
        pass
    @abstractmethod
    def delete_product(self,Product_id):
        pass

class ProductManager(ProductAbstract):
    def create_product(self,Product):
        print("This is a new product called " + (Product.Product_name) )
    
    def edit_product(self,Product_id):
        print("This product is edited")

    def get_product_by_id(self,Product_id):
        print("Your product id is " + f"{Product_id}" )

    def get_all_products(self):
        print("Get all products here")

    def upload_product_image(self,Product_id,Product_image):
        print ("Get product image here")

    def delete_product(self,Product_id):
        print("click here, to delete product")

new_product=ProductManager()
new_product.create_product(Product)
new_product.get_product_by_id(73)
new_product.edit_product(73)
new_product.get_all_products()
new_product.upload_product_image(73,"")
new_product.delete_product(73)
