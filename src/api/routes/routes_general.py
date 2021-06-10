#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp

route_path_general = Blueprint("route_path_general", __name__)

@route_path_general.route('/v1.0/hi', methods=['GET'])
def hi():
    """
    Get hello
    ---
    responses:
            200:
                description: Returns a hello
                schema:
                  hi: string
    """
    return response_with(resp.SUCCESS_200, value={"hi": "helloWorld"})