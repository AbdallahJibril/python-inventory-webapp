from code_python.file_manager import File_manager
from code_python.product import Product
class Product_manager :
   def __init__(self):
       self.F_M = File_manager()
       self.read_file = self.F_M.read_file()
   def add_product(self,name,price,qty):
        self.name = name
        self.price= price
        self.qty  = qty
        self.products = []
        self.products.append(Product(self.name,self.price,self.qty).to_dict())
        self.F_M.seve(self.products)
   def update_True_False(self,name_product):
       self.name_product = name_product
       if self.name_product not in self.F_M.names_products():
           return print(f"✖️ The product '{self.name_product}' is not available. Choose from: {self.F_M.names_products()}\n")
       elif self.name_product in self.F_M.names_products():
           return True
       else:
           return print("Unknown error✖️✖️✖️\n")
   def update_name(self ,Variabl_product_name, New_name):
       self.Variabl_product_name =Variabl_product_name
       self.New_name = New_name
       self.F_M.update_name1(self.Variabl_product_name,self.New_name)
   def update_price(self ,Variabl_product_name, New_price):
       self.Variabl_product_name =Variabl_product_name
       self.New_price = New_price
       self.F_M.update_price1(self.Variabl_product_name,self.New_price)
   def update_quantity(self ,Variabl_product_name, New_quantity):
       self.Variabl_product_name =Variabl_product_name
       self.New_quantity = New_quantity
       self.F_M.update_quantity1(self.Variabl_product_name,self.New_quantity)
   def Delete_product(self,name_to_Delete):
       self.name_to_Delete = name_to_Delete
   def View_products(self):
       return self.F_M.read_file()
