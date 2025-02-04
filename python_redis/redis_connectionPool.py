import redis
from redis import ConnectionPool

pool = ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

pool = ConnectionPool(host='localhost', port=6379, db=0)

r1 = redis.Redis(connection_pool=pool)
r2 = redis.Redis(connection_pool=pool)

r.set('user:1:name', 'Adrien')
r1.set('user:2:name', 'John Doe')
r2.set('user:3:name', 'Alice')

print(r.get('user:1:name').decode('utf-8'))
print(r1.get('user:2:name').decode('utf-8'))
print(r2.get('user:3:name').decode('utf-8'))

values = r.mget(['user:1:name', 'user:2:name', 'user:3:name'])
print([value.decode('utf-8') for value in values])