'''
Tömegközlekedés

Adott járaton minden megálló után megszámoljuk az utasokat
(felszállók, leszállók) az egyes járatokon a megállók száma fix.
A járat az út végén feltölti a mérést es az időpontot.
Az egyes járatokon mennyi az átlagos forgalom?
Melyik megállókon van sok felszálló / leszálló?

{
    "jarat1: "[
        {
            "megallo": "megallo1",
            "timestamp": "10:00",
            "felszallok": 10,
            "leszallok": 3
        },
        {
            "megallo": "megallo2",
            "timestamp": "10:20",
            "felszallok": 22,
            "leszallok": 43,
        }
    ]
}
'''
import db
from flask import request, Blueprint, Flask
import sample
import statistics_ as st

app = Flask(__name__)

db_api = Blueprint('db', __name__)


@db_api.route('/ping')
def health_check():
    return '1'


@db_api.route("/add-route-data/<bus_id>", methods=['POST'])
def add_route_data(bus_id):
    return db.add_route_data(bus_id, request.get_json())


@db_api.route('/get-sample-data', methods=['GET'])
def get_sample_data():
    resp = dict()
    resp['data'] = sample.get_sample_data()
    return resp


@db_api.route('/statistics/passengers')
def get_average_passengers_by_route():
    return st.average_passengers_by_route()


@db_api.route('/statistics/boarding')
def get_max_boarding_and_landing_passengers():
    r = st.max_boarding_and_landing_passengers(request.args)
    return r


def createTestClient():
    return app.test_client()


app.register_blueprint(db_api)
