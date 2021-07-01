from os import error
from flask import Flask, request
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import flask_restful
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

class Home(Resource):
  def get(self):
    return {'message': 'This is homepage.'}
  def post(self):
    return {'message': 'This is homepage.'}
  def put(self):
    return {'message': 'This is homepage.'}
  def delete(self):
    return {'message': 'This is homepage.'}
  def patch(self):
    return {'message': 'This is homepage.'}

class Example(Resource):
  def get(self):
    return {'content': all_entry}, 200
  def post(self):
    return {'message': 'Under Development'}, 404
  def put(self):
    parser = reqparse.RequestParser()# initialize
    parser.add_argument('key', required=True)
    args = parser.parse_args()# parse argument to dictionary
    return {'message': 'Something Went Wrong in Validation. If this error presists please visit the docs.'}, 401
  def delete(self):
    return {'message': 'Unauthorized'}, 405
  def patch(self):
    return
