from flask.helpers import send_file
import db
import pandas as pd
import uuid
import numpy as np


def average_passengers_by_route():
    filename = generate_filename()
    bus = db.get_bus_data()
    all = list()
    for i in bus:
        b = list(map(lambda x: x['felszallok'], bus[i]))
        all.append(np.average(b))
    df = pd.DataFrame({
        'keys': bus.keys(),
        'avg': all
    })

    ax = df.plot.bar(x='keys', y='avg', label='Atlag')
    ax.set_xlabel('Jaratok')
    ax.set_ylabel('Utasok')
    ax.set_title('Atlagos utasforgalom jaratonkent')
    ax.figure.savefig(filename)
    return send_file(filename, 'image/png')


def max_boarding_and_landing_passengers(args):
    filename = generate_filename()
    bus = db.get_bus_data()
    boarding = list()
    landing = list()
    for i in bus:
        boarding_passengers = list(map(lambda x: x['felszallok'], bus[i]))
        landing_passengers = list(map(lambda x: x['leszallok'], bus[i]))
        boarding.append(np.amax(boarding_passengers))
        landing.append(np.amax(landing_passengers))

    df = pd.DataFrame({
        'Felszallok': boarding,
        'Leszallok': landing,
    }, index=bus.keys())

    ax = df.plot.bar()
    ax.set_xlabel('Jaratok')
    ax.set_ylabel('Utasok')
    ax.set_title('Maximum felszallok es leszallok jaratonkent')
    ax.figure.savefig(filename)
    return send_file(filename, 'image/png')


def generate_filename() -> str:
    return uuid.uuid4().hex.upper()[0:6]+'.png'
