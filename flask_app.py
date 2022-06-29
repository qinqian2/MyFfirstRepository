
from flask import Flask, request, session
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS


app = Flask(__name__)
app.secret_key='ceshi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qinqian.1234@127.0.0.1:3306/jeesite'
cors=CORS(app)
api=Api(app)
db = SQLAlchemy(app)
# SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_COMMIT_TEARDOWN = True
app.config['SECRET_KEY'] = 'ceshi'
jwt = JWTManager(app)


class User(db.Model):
    __tablename__='user_qq'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=False)
    password = db.Column(db.String(80), unique=False)

    def __repr__(self):
        return '<User %r>' % self.username

class TestCase(db.Model):
    __tablename__='user_testcase'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    desc = db.Column(db.String(120), unique=True)
    data = db.Column(db.String(120), unique=True)

    uid=db.Column(db.Integer,db.ForeignKey('user_qq.id'),nullable=False)
    user=db.relationship('User',backref=db.backref('testcases',lazy=True))

    def __repr__(self):
        return '<TestCase %r>' % self.name

class HelloWorld(Resource):
    def get(self):
        return {'data': 'hello for qq'}

class Login(Resource):
    def get(self):
        return {'data':'login info'}

    def post(self):
        user=User.query.filter_by(username= request.form['username'],password=request.form['password']).first()
        if user is None:
            return {
                'data':'','errcode':1
            }
        else:
            access_token=create_access_token(identity=user.username)
            return {
                'data':{
                'username':user.username,
                'password':user.password,
                'token':access_token
                },
                'errcode':0
            }

    def delete(self):
        pass

class Project(Resource):
    def get(self):
        pass

class TestCaseResource(Resource):

    def get(self):
        testcases=TestCase.query.all()
        app.logger.info(testcases)
        res=[{
            'id':t.id,
            'name':t.name,
            'desc':t.desc,
            'data':t.data
        }for t in testcases]
        return {
            'data':res,
            'errcode':0
        }

    def put(self):
        app.logger.info(request.json)
        testcase=TestCase.query.filter_by(id=request.json['id']).first()
        testcase.name=request.json['name']
        testcase.desc=request.json['desc']
        db.session.flush()
        db.session.commit()

        testcase2 = TestCase.query.filter_by(id=request.json['id']).first()
        app.logger.info(testcase2)
        app.logger.info(testcase2.name)
        return ""

class LoginResource(Resource):
    def get(self):
        username=get_jwt_identity()
        app.logger.info(username)
        user=User.query.filter_by(username=username).first()
        app.logger.info(user)
        if user is None:
            return 'not login'
        else:
            return {
                'id':user.id,
                'name':user.username
            }

    def post(self):
        app.logger.info(request.json)
        username=request.json['username']
        password=request.json['password']
        user = User.query.filter_by(username=username, password=password).first()
        session["user"]=user.username
        access_token = create_access_token(identity=user.username)
        if user is None:
            return {
                'data': '',
                'errcode': 1
            }
        else:
            return {
                    'data': {
                        'username': user.username,
                        'password': user.password,
                        'token': access_token
                    },
                    'errcode': 0
                }

    def delete(self):
        session["user"]=""
        return "logout"

# api.add_resource(HelloWorld, '/')
# api.add_resource(Login,'/login')
# api.add_resource(Project,'/project')
# api.add_resource(TestCase,'/testcase')
api.add_resource(TestCaseResource, '/testcase')
api.add_resource(LoginResource, '/login')

if __name__ == '__main__':
    app.run(debug=True)