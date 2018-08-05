# -*- coding: utf-8 -*-

from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)
APP_URL = "http://127.0.0.1:5000"


class CrimeGeo(Resource):
    def get(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument('latitude', type=float, help="Latitude of the user")
        parser.add_argument('longitude', type=float, help="Longitude of the user")

        args=parser.parse_args()
        latitude=float(args["latitude"])
        longitude=float(args["longitude"])
#
        cursor = mongo.db.redFinal.find({"location":{"$nearSphere":{"$geometry":{"type":"Point", "coordinates":[ longitude, latitude ] }, "$maxDistance": 5000}}})
        cursor2 = mongo.db.speedFinal.find({"location":{"$nearSphere":{"$geometry":{"type":"Point", "coordinates":[ longitude, latitude ] }, "$maxDistance": 5000}}})
	
        sum_red = 0
        sum_speed = 0
        is_school_zone = False

#	Count needs to be judged and something returned 
        for crime in cursor:
            print(crime)
            sum_red += crime['count']
            if crime['schoolZone'] == 'Y':
                is_school_zone = True
        

        for crime in cursor2:
            print(crime)
            sum_speed += crime['count']
            if crime['schoolZone'] == 'Y':
                is_school_zone = True

        return jsonify({"Red_Lights": str(sum_red), "Speeding": str(sum_speed), "School_Zone": str(is_school_zone)})

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

