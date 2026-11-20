import redis

client = redis.Redis(host="localhost", port=6379, decode_responses=True)

client.set("session:2001", "active", ex=60)
print("session:", client.get("session:2001"), "ttl:", client.ttl("session:2001"))

client.hset("user:2001", mapping={"name": "Grace Hopper", "role": "engineer"})
print("user:", client.hgetall("user:2001"))

client.zadd("leaderboard", {"ada": 120, "grace": 90, "edsger": 150})
print("top:", client.zrevrange("leaderboard", 0, -1, withscores=True))

client.lpush("queue:jobs", "job-1", "job-2")
print("job:", client.rpop("queue:jobs"))
