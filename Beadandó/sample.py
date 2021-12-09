import random
import datetime


stops = ['megallo1', 'megallo2', 'megallo3', 'megallo4', 'megallo5']


def get_sample_data() -> list:
    bus = list()
    start_time = datetime.datetime(
        2021, 12, 10, random.randint(8, 19), random.randint(0, 59))
    for i in stops:
        start_time = start_time + \
            datetime.timedelta(minutes=random.randint(8, 19))
        b = dict()
        b['megallo'] = i
        b['timestamp'] = start_time.strftime('%H:%M')
        b['felszallok'] = random.randint(0, 60)
        b['leszallok'] = random.randint(0, 50)
        bus.append(b)
    return bus
