import pandas as pd
import os
class File_manager:
    def __init__(self):
        self.filname ="products.csv" # اسم الملف 
        self.mm()
    def mm(self):
        if not os.path.exists(self.filname):    # هل الملف موجود ؟
            columns =["ID","product", "price", "quantity" ,"total"] # اسماء العواميد داخل الملف 
            df2 = pd.DataFrame(columns=columns)
            df2.to_csv(self.filname,index=False)
    def read_file(self):
        
        if not pd.read_csv(self.filname).values.tolist():
            return "No products available to update ✖️\n"
        else:
            return pd.read_csv(self.filname).to_dict(orient="records")
    def seve (self,products):  

        df = pd.read_csv(self.filname)
        if df.empty:
            new_ID =1
        else:
            new_ID =df["ID"].max() + 1
        products[0]["ID"] =new_ID
        naw_df =pd.DataFrame(products)     # الداتا الجديده 
        old_df = pd.read_csv(self.filname)      # الداتا القديمه 
        final_df = pd.concat([old_df,naw_df],ignore_index=True) # الداتا الجديده و القديمه
        final_df.to_csv(self.filname,index=False) # اضافه الجميع داخل الملف تاني 
    def update_name1(self,Old_name,New_name):
        self.Old_name =Old_name
        self.New_name =New_name
        df =pd.read_csv(self.filname)
        df.loc[df["product"] == self.Old_name,"product"] = self.New_name
        df.to_csv(self.filname,index=False)
    def update_price1(self,name_product,to_price):
        self.name_product =name_product
        self.to_price =to_price
        df =pd.read_csv(self.filname)
        df.loc[df["product"] == self.name_product,"price"] = self.to_price
        df.loc[df["product"] == self.name_product,"total"] = self.to_price * df.loc[df["product"] == self.name_product,"quantity"]
        df.to_csv(self.filname,index=False)
    def update_quantity1(self,name_quantity,New_quantity):
        self.name_quantity =name_quantity
        self.New_quantity =New_quantity
        df =pd.read_csv(self.filname)
        df.loc[df["product"] == self.name_quantity,"quantity"] = New_quantity
        df.loc[df["product"] == self.name_quantity,"total"] = New_quantity * df.loc[df["product"] == self.name_quantity,"price"]
        df.to_csv(self.filname,index=False)
    def Delete(self,Dlt):
        self.name =Dlt
        if not pd.read_csv(self.filname).values.tolist():
            return print("No products available to delete ✖️\n")
        else:
            if self.name in self.names_products():
                df = pd.read_csv(self.filname)
                df =df[df["product"]!= self.name]
                df.to_csv(self.filname,index=False)
            else:
                print("✖️✖️✖️")
    def names_products (self):
        names =pd.read_csv(self.filname)
        return  names["product"].to_list()
