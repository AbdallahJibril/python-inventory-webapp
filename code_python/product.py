import pandas as pd
class Product:
    def __init__(self,name,price,qty):
        self.name = name
        self.price= price
        self.qty  = qty
        self.total= self.price * self.qty 
    def to_dict(self):
        return{
            "product" :self.name,
            "price":self.price,
            "quantity"  :self.qty,
            "total":self.total,
        }
