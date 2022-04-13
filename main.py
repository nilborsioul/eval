from bottle import route, run
from helpers import addition
import sys


@route("/add/<a>/<b>")
def routeaddition(a, b):
    return addition(a, b)


run(host="0.0.0.0", port=sys.argv[1], reloader=True)
