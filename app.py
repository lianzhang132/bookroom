from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import book
from views import author

from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager

app = Flask(__name__)
manager = Manager(app)
app.register_blueprint(book.book)
app.register_blueprint(author.author)
@app.route('/')
def hello_world():
    return 'Hello World!'

# 数据库配置链接
app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:666666@localhost:3306/flask1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#设置数据库追踪信息,压制警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# datas = Blueprint('datas',__name__,url_prefix="/datas",template_folder="datas_template")
db = SQLAlchemy(app)

#第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
migrate = Migrate(app,db)

#manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令 db 自定义 只是一个命令
manager.add_command('db',MigrateCommand)

class Author(db.Model):
    __tablename__ = 'author'
    author_id = db.Column(db.Integer,primary_key=True)
    author_name = db.Column(db.String(20),unique=True)

    books = db.relationship('Book',backref='aus')

# 书籍
class Book(db.Model):
    __tablename__ = 'book'
    book_id = db.Column(db.Integer,primary_key=True)
    book_title = db.Column(db.String(20),unique=True)

    authors_id = db.Column(db.Integer, db.ForeignKey('author.author_id'))

tb_student_course = db.Table('tb_student_course',
                             db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
                             db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
                             )


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    age = db.Column(db.String(3), unique=True)

    courses = db.relationship('Course', secondary=tb_student_course,
                              backref='student',
                              lazy='dynamic')


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # score = db.Column(db.String(64), unique=True)



#
# db.drop_all()
# db.create_all()


if __name__ == '__main__':
    manager.run()
