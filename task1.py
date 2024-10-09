import queue
import random
import time

request_queue = queue.Queue()

def generate_request():
    request_id = random.randint(1, 1000)
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги")

def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Заявка {request_id} оброблена")
    else:
        print("Черга порожня")

while True:
    generate_request()
    process_request()
    time.sleep(1)