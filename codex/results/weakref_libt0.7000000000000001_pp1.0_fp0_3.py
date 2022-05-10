import weakref
from typing import List

from flask import Flask
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from flask_restful import fields

from utils.flask_utils import output_json


class TodoItem(Resource):
    def get(self, todo_id):
        # type: (int) -> Dict[str, str]
        return {todo_id: TodoDAO.todos[todo_id]}

    def put(self, todo_id):
        # type: (int) -> Dict[str, str]
        TodoDAO.todos[todo_id] = request.form['data']
        return {todo_id: TodoDAO.todos[todo_id]}


class TodoDAO(object):
    __metaclass__ = abc.ABCMeta
    todos = {}

    @classmethod
    def get(cls, todo_id):
        # type: (int) -> Dict[str, str]
       
