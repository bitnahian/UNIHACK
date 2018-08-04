# -*- coding: utf-8 -*-

from flask import Flask, jsonify, url_for, redirect, request
# from flask_pymongo import PyMongo
from flask_restful import Api, Resource

app = Flask(__name__)
# app.config["MONGO_DBNAME"] = "crimegeo_db"
# mongo = PyMongo(app, config_prefix='MONGO')
APP_URL = "http://127.0.0.1:5000"


class CrimeGeo(Resource):
    def get(self):
#        data = []
#
#        cursor = mongo.db.student.find({}, {"_id": 0, "update_time": 0}).limit(10)
#
#        for student in cursor:
#            print student
#            student['url'] = APP_URL + url_for('crimegeo') + "/" + student.get('registration')
#            data.append(student)

        return jsonify({"data":"Hello"})

#    def post(self):
#        data = request.get_json()
#        if not data:
#            data = {"response": "ERROR"}
#            return jsonify(data)
#        else:
#            registration = data.get('registration')
#            if registration:
#                if mongo.db.student.find_one({"registration": registration}):
#                    return {"response": "student already exists."}
#                else:
#                    mongo.db.student.insert(data)
#            else:
#                return {"response": "registration number missing"}
#
#        return redirect(url_for("crimegeo"))
#
#    def put(self, registration):
#        data = request.get_json()
#        mongo.db.student.update({'registration': registration}, {'$set': data})
#        return redirect(url_for("crimegeo"))
#
#    def delete(self, registration):
#        mongo.db.student.remove({'registration': registration})
#        return redirect(url_for("crimegeo"))
#

class Index(Resource):
    def get(self):
        return redirect(url_for("crimegeo"))


api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(CrimeGeo, "/api", endpoint="crimegeo")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

