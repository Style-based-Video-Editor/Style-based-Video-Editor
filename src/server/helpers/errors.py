# flask packages
from flask import Response, jsonify


def file_is_reqired() -> Response:
    output = {
        "error": {"msg": "You must upload an image."}}
    resp = jsonify({'result': output})
    resp.status_code = 400
    return resp


def extention_allowed_only(extention) -> Response:
    output = {
        "error": {"msg": "Only these extentions is allowed {}.".format(extention)}}
    resp = jsonify({'result': output})
    resp.status_code = 400
    return resp


def unauthorized() -> Response:
    output = {"error":
              {"msg": "401 error: The email or password provided is invalid."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 401
    return resp


def forbidden() -> Response:
    output = {"error":
              {"msg": "403 error: The current user is not authorized to take this action."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 403
    return resp


def invalid_route() -> Response:
    output = {"error":
              {"msg": "404 error: This route is currently not supported. See API documentation."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp
