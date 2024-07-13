from flask import jsonify

DEFAULT_HEADERS = {"Content-Type": "application/json"}


def make_response(data, status=200, headers=None):
    return (
        jsonify(data),
        status,
        DEFAULT_HEADERS,
    )
def not_authorized_error():
    return make_response({"message": "Unauthorized"}, 401)

def error(err_code_str,message_str=None, code=500):
    payload = {"error": err_code_str}
    if message_str:
        payload["message"] = message_str

    return make_response(payload, code)

def not_found():
    return error("not found", code=404)


def internal_error(err):
    return error("An internal error occurred", code=500)