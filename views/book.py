# 1.导入蓝图类
from flask import Blueprint,render_template

# 2.蓝图对象创建完成
book = Blueprint('book',__name__,url_prefix='/book',template_folder="book_template")

# 3.蓝图路由
@book.route('/goods_list',methods=['get','post'])
def book_list():


    return 'book_list'


# 3.蓝图路由
@book.route('/add',methods=['get','post'])
def add():

    return render_template("authoradd.html")


