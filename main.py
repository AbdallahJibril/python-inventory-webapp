from product_manager import Product_manager
from file_manager import File_manager
P_M = Product_manager()
def input_number (masg):
    while True:
      try :
          value =float( input(masg))
          return value
      except ValueError:
         print("error anter number ✖️")
print("""
      ___****___***___***___***___***

      Welcome to the bill calculator

      ___****___***___***___***___***
      """)
while True:
    dark = input("""
                 
                 1-Add product
                 2-View products
                 3-update product
                 4-Delete product
                 5-Stop
                                               Choose(1-2-3-4-5)
                 """)
    if   dark =="1":
        jj = True
        while jj:
          Product_name=          input("Product name: ")
          Product_price=         input_number("Product price: ")
          Product_quantity=        input_number("Product quantity: ")
          P_M.add_product(Product_name,Product_price,Product_quantity)
          print("\n✅✅✅✅✅✅\n")
          while True:
            cccc=input("Are there any other products you would like to add?[y , n]:  ")
            if cccc=="y":   
                    break
            elif cccc=="n":
                    jj = False
                    break
            else:
                    print("Wrong choice✖️....! \n\n")
    elif dark =="2":
        P_M.View_products()
    elif dark =="3":
        while True:
            input_product_name = input("Product name you want to update  (or type 'stop' to exit):.. ").lower()
            if P_M.update_True_False(input_product_name):
                while True:
                    dd = input("\nType_of_change Choose (name / price / Qty) (or type 'stop' to exit)..... ").lower()
                    if   dd =="name":
                        P_M.update_name(input_product_name,input("New name....").lower())
                        break
                    elif dd =="price":
                        P_M.update_price(input_product_name,input_number("New price...."))
                        break
                    elif dd =="quantity":
                        P_M.update_quantity(input_product_name,input_number("New quantity...."))
                        break
                    elif dd =="stop":
                        break
                    else:
                      print("\n✖️ Invalid option! Choose (name / price / Qty) (or type 'stop' to exit).\n")
            elif input_product_name == "stop":
                break
    elif dark =="4":
        File_manager().Delete(input())
    elif dark =="5":
       break
    else:
      print("Error✖️  Choose(1-2-3-4-5)")
