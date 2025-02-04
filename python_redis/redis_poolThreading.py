import redis
from redis import ConnectionPool
import threading

pool = ConnectionPool(host='localhost', port=6379, db=0)

def worker():
    r = redis.Redis(connection_pool=pool)
    r.set('user:1:name', 'Adrien')
    result = r.get('user:1:name')
    print(f"Résultat récupéré par {threading.current_thread().name}: {result.decode('utf-8')}")

threads = [threading.Thread(target=worker, name=f"Thread-{i+1}") for i in range(5)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
