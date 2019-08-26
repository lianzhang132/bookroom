from flask import Flask,request,render_template,jsonify


app = Flask(__name__)
@app.route('/')

def hello():
    return render_template("fo.html")

@app.route('/login',methods=['post'])
def login():
    num1 = 1
    num2 = 1
    num3 = num1/num2
    # print(request.args.get('x'))
    # post man 传递数据的时候 是以post 形式发送数据,参数 却是以get形式传,类似于 form表单中action 里面路径后面传递的参数
    # uname = request.args.get('uname')
    # upass = request.args.get('upass')
    uname = request.form.get('uname')
    upass = request.form.get('upass')
    # print(uname)
    # print(upass)
    # 用户 没有填写 用户名 或者 密码
    if not all([uname,upass]):
        # 用户不能登录
        result = {
            'errcode':1,
            'errmsg':'用户名和密码 是空'
        }
        return jsonify(result)

    # 查询数据库 判断用用户密码是否正确
    if uname == 'xiaoming' and upass =='123456':
        # 可以登录
        result = {
            'errcode': 0,
            'errmsg': '登录成功'
        }
        return jsonify(result)
    else:
        # 不能登录
        result = {
            'errcode': 2,
            'errmsg': '用户名和密码错误'
        }
        return jsonify(result)




if __name__ == '__main__':

    app.run(debug=True)
