import boto3, time, ftplib, sys, zlib, struct
from flask import Flask, request
from flask_restful import Resource, Api
from ftplib import FTP
from io import BytesIO
import importlib as il

app = Flask(__name__)
api = Api(app)

class sample(Resource):
	def get(self):
		return 'hello world'

api.add_resource(sample, '/hello/')


if __name__ == '__main__':
     app.run(port='5002')
