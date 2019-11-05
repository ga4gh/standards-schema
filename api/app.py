import json
from flask import Flask, request, Response
from api.loaders.loader import Loader
app = Flask(__name__)

loader = Loader()
loader.load()

@app.route("/standards/<standard_id>")
def get(standard_id):

    resp = Response()
    resp.headers['Content-Type'] = "application/json"
    resp.headers['Access-Control-Allow-Origin'] = "*"
    if standard_id in loader.data.keys():
        resp.status_code = 200
        resp.set_data(json.dumps(loader.data[standard_id]))
    else:
        resp.status_code = 404
        resp.set_data(json.dumps({
            "message": "Standard not found"
        }))

    return resp

@app.route("/standards/search")
def search():

    standards_keys = list(loader.data.keys())
    search_params = [
        {
            "param_name": "workstream",
            "get_value_method": lambda std: std["primary_workstream"]["name"]
        }
    ]
    for search_param in search_params:
        param_name = search_param["param_name"]
        get_value_method = search_param["get_value_method"]
        search_val = request.args.get(param_name)

        if search_val:
            for standard_key in [a for a in standards_keys]:
                standard = loader.data[standard_key]
                standard_val = get_value_method(standard)

                if search_val != standard_val:
                    standards_keys.remove(standard_key)

    return_objs = [loader.data[k] for k in standards_keys]
    body = json.dumps(return_objs)
    resp = Response(body)
    resp.headers['Content-Type'] = "application/json"
    resp.headers['Access-Control-Allow-Origin'] = "*"
    return resp
