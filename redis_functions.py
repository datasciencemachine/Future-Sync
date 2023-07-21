import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
def get_redis_client():
    """Gets a Redis client."""
    return r

def set_state(macid, state):
    """Sets the state of a device in Redis."""
    redis_client = get_redis_client()
    redis_client.set(macid, state)

def get_state(macid):
    """Gets the state of a device from Redis."""
    redis_client = get_redis_client()
    state = redis_client.get(macid)
    return state
