import threading
import queue
import db
from datetime import datetime

q = queue.Queue()


def run_statistics_job():
    q.put((route_time_summary, []))
    return True


def execute_background_process():
    while True:
        f, args = q.get()
        f(*args)


def route_time_summary():
    data = db.get_bus_data()
    for bus in data:
        start_time = data[bus][0]['timestamp']
        end_time = data[bus][(len(data[bus]) - 1)]['timestamp']
        start_time = datetime.strptime(start_time, "%H:%M")
        end_time = datetime.strptime(end_time, "%H:%M")
        difference = (int)((end_time - start_time).seconds / 60)
        db.client[db.DB_NAME]['statistic'].update_one(
            {
                "_id": bus
            },
            {
                "$set": {
                    "menetido": difference
                }
            }, True)


threading.Thread(target=execute_background_process, daemon=True).start()
