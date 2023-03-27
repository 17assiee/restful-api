from flask import Flask
from flask_restful import Api, Resource, reqparse

ser = Flask(__name__)
api = Api()

students = {
    1: {"name": "Asiya", "age": 19},
    2: {"name": "ALI", "age": 18}
}

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("age", type=int)


class Main(Resource):
    def get(self, student_id):
        if student_id == 0:
            return students
        else:
            return students[student_id]

    def delete(self, student_id):
        del students[student_id]
        return students

    def post(self, student_id):
        students[student_id] = parser.parse_args()
        return students

    def put(self, student_id):
        students[student_id] = parser.parse_args()
        return students


api.add_resource(Main, "/api/students/<int:student_id>")
api.init_app(ser)

if __name__ == "__main__":
    ser.run(debug=True, port=3000, host="127.0.0.1")
