from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__, static_url_path='')
app.secret_key = 'why would I tell you my secret key?'
api = Api(app)
tasks = {}


@app.route('/')
def root():
    return app.send_static_file('index.html')


class Task(Resource):
    @staticmethod
    def get(task_id):
        results = {}
        try:
            results = json.loads(tasks[task_id])
        except ValueError, e:
            results = tasks[task_id]
        else:
            results = tasks[task_id]
        return results, 201

    @staticmethod
    def post(task_id):
        tasks[task_id] = request.data
        return tasks[task_id], 204, {'Access-Control-Allow-Origin': '*'}

api.add_resource(Task, '/<string:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
