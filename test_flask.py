from flask_app import db,User

def test_flask():
    admin = User(username='admin', email='admin@example.com' ,password='123')
    db.session.add(admin)
    db.session.commit()

{
    "data": {
        "username": "admin",
        "email": "admin@example.com",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NDY3NDc1NCwianRpIjoiZTk5MjZkYzktZDFlZi00OGQxLWJiNTAtZTAxYmIyYzljN2Y1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNjU0Njc0NzU0LCJleHAiOjE2NTQ2NzU2NTR9.R6ISzysxiGmzyS5NM57fU4CHXIjE5Ax5BQAiUTMlOCQ"
    },
    "errcode": 0
}
