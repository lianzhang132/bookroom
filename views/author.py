# 1.导入蓝图类
from flask import Blueprint,render_template,request,redirect,url_for,g
# from app import db,Author,Book
# 2.蓝图对象创建完成
author = Blueprint('author',__name__,url_prefix='/author',template_folder="author_template")

# 3.蓝图路由
@author.route('/authors_list',methods=['get','post'])
def author_list():
    author_lis = g.Author.query.all()

    return render_template('author_list.html',author_lis=author_lis)


# 3.蓝图路由
@author.route('/add',methods=['get','post'])
def add():
    if request.method == 'POST':
        # 获取作者的值
        auth_name = request.form.get('auth_name')
        # 根据autho_name 去查询 作者是否已经被添加过
        res = g.Author.query.filter_by(auth_name=auth_name).first()
        if not res:

            # 添加
            try:
                # 实例化一个author 对象
                auth = g.Author(auth_name=auth_name)
                # 添加作者
                g.db.session.add(auth)
                g.db.session.commit()
                # 所有的数据处理准备好之后，执行commit才会提交到数据库！
                try:
                    book_name = request.form.get('book_title')
                    bo = g.Book(book_title=book_name, author_id=auth.author_id)
                    # 添加书籍
                    g.db.session.add(bo)
                    g.db.session.commit()
                except Exception as e:
                    # 加入数据库commit提交失败，必须回滚！！！
                    g.db.session.rollback()
                    raise e

            except Exception as e:
                # 加入数据库commit提交失败，必须回滚！！！
                g.db.session.rollback()
                raise e
        else:
            # 作者已经被添加过 获取作者id
            id = res.author_id
            try:
                book_name = request.form.get('book_title')
                bo = g.Book(book_title=book_name, author_id=id)
                # 添加书籍
                g.db.session.add(bo)
                g.db.session.commit()
            except Exception as e:
                # 加入数据库commit提交失败，必须回滚！！！
                g.db.session.rollback()
                raise e
        # 跳转到作者列表页面
        return redirect(url_for("author_list"))

    return render_template("authoradd.html")
