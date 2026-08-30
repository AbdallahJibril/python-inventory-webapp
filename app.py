from code_python.product_manager import Product_manager
from code_python.file_manager import File_manager
from flask import Flask ,render_template,request, session,url_for,redirect ,flash
app =Flask(__name__)
app.secret_key = "123"
app.secret_key ="secret123"
P_M = Product_manager()
def input_number (masg):
    while True:
      try :
          value =float( input(masg))
          return value
      except ValueError:
         print("error anter number ✖️")
Choose= ["Add product","View products","update product","Delete product"]
type_update=["name","price","quantity"]
@app.route("/")# فتح صفحه يندكس وختيار من Choose
def index():
   return render_template("index.html" ,Choose=Choose)
@app.route("/inputs" ,methods=["POST"])#  اخذ الامر وتنفيذه (عرض اضافه تحديث لخ..)
def inputs():
    Dark =request.form.get("choice")
    if Dark in Choose:
       if Dark =="Add product":
          return render_template("add_input.html")
       elif Dark=="View products":
           View_file=P_M.View_products()
           
           return    render_template("view_products.html" , view_file=View_file)
       elif Dark=="update product":
          return render_template("update_input.html",names_products=File_manager().names_products())
       elif Dark=="Delete product":
          return render_template("delete.html",names_products=File_manager().names_products())
    else:
       return "ادخل قيمه"
@app.route("/add" , methods=["POST"])# نرجع صفحه لاخذ بينات المنتج 
def add_product():
   name =request.form.get("name")
   if name  in File_manager().names_products():
 
            flash(" هذا المنتج موجود لا يمكن اضافته ✖️")
            return redirect(url_for('index'))
   else: 
       try :
            price =float( request.form.get("price"))
            quantity =float(request.form.get("quantity"))
            P_M.add_product(name , price , quantity)
            flash("تمت إضافة المنتج بنجاح ✅")
            return redirect(url_for('index'))
       except ValueError:
             return "ادخل رقم "
@app.route("/name_update", methods=["POST"])# (في حاله التحديث نرجع لو كان اسم المنتج صح    (تحديث  
def name_update():
    session ["name_product"] =request.form.get('name_product')
    if str (request.form.get('name_product')) in File_manager().names_products():
          return render_template("update_type.html" ,type_update=type_update)
    else:
        return " قيمه خطا  "
@app.route("/types_update", methods=["POST"]) # تابع التحديث
def types_update():
      session ["name_type"] =request.form.get('update_type')
      if request.form.get('update_type') =="name":
            return render_template("new_name.html")
      elif request.form.get('update_type') =="price":
            return render_template("new_price.html")
      elif request.form.get('update_type') =="quantity":
            return render_template("new_quantity.html")
      return "قيمه خطا "
@app.route("/type_N_P_Q", methods=["POST"])# تابع التحديث  
def type_N_P_Q():
      name_product =session["name_product"]
      name_type =session["name_type"]
      if name_type=="name":
            P_M.update_name(name_product,str(request.form.get("new_name")))
            flash("تم تحديث المنتج بنجاح ✏️")
            return render_template("index.html" ,Choose=Choose)
      elif name_type=="price":
         try :
            price =float( request.form.get("new_price"))
            P_M.update_price(name_product,price)
            flash("تم تحديث المنتج بنجاح ✏️")
            return render_template("index.html" ,Choose=Choose)
         except ValueError:
          flash("اكتب رقم")
          return render_template("index.html",Choose=Choose)
      elif name_type=="quantity":
            try :
               quantity =float( request.form.get("new_quantity"))
               P_M.update_quantity(name_product,quantity)
               flash("تم تحديث المنتج بنجاح ✏️")
               return render_template("index.html",Choose=Choose)
            except ValueError:
                 flash("اكتب رقم")
                 return render_template("index.html",Choose=Choose)
      return "قيمه خاطا "
@app.route("/Delete", methods=["POST"])
def Delete():
    print(str (request.form.get("name_D")))
    if str (request.form.get('name_D')) in File_manager().names_products():
        File_manager().Delete(str(request.form.get("name_D")))
        flash("تم حذف المنتج بنجاح 🗑")
        return render_template("index.html" ,Choose=Choose)
    else:
        return "خطا ادخل اسم صحصح"

if __name__ == "__main__":
    app.run(debug=True)