<div align="center">
<img src="assets/brand-logo.svg" alt="Arya Fatthurahman" width="120" />
</div>

# Redis Lab

<sub>Run Redis 8 in Docker and practice strings, hashes, lists, sorted sets, expiry, and a small Python client.</sub>

<p>
  <img src="https://img.shields.io/badge/Database-Redis-DC382D?style=flat-square" alt="Database: Redis" />
  <img src="https://img.shields.io/badge/Category-Key--value%20%2F%20cache-6366F1?style=flat-square" alt="Category: Key-value / cache" />
  <img src="https://img.shields.io/badge/Runs%20in-Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Runs in Docker" />
  <img src="https://img.shields.io/badge/License-MIT-22C55E?style=flat-square" alt="License: MIT" />
  <a href="https://github.com/devarent/redis-lab/actions/workflows/compose-check.yml"><img src="https://github.com/devarent/redis-lab/actions/workflows/compose-check.yml/badge.svg" alt="compose-check" /></a>
</p>

## What this lab is

Redis is the default answer for caching, sessions, rate limits, and lightweight queues. This lab starts a persistent Redis instance, gives you a command cheat sheet, and includes a Python client so you can see the same operations from application code.

## Quickstart

```bash
docker compose up -d
docker compose exec redis redis-cli
# paste commands from examples/commands.redis, or run the Python client:
python -m pip install redis
python examples/redis_client.py
```

## Connection details

| Field | Value |
| --- | --- |
| Host | `localhost` |
| Port | `6379` |
| URL | `redis://localhost:6379/0` |
| Password | `(none in this lab)` |
| CLI | `docker compose exec redis redis-cli` |

## Examples

| File | What it shows |
| --- | --- |
| [`docker-compose.yml`](docker-compose.yml) | Engine, ports, and persistent volume. |
| [`.github/workflows/compose-check.yml`](.github/workflows/compose-check.yml) | Validates the Compose file on every push. |
| [`examples/commands.redis`](examples/commands.redis) | Core data structures and expiry commands. |
| [`examples/redis_client.py`](examples/redis_client.py) | The same operations from Python with redis-py. |

## Exercises

1. Implement a fixed-window rate limiter with `INCR` and `EXPIRE`.
2. Cache a slow function result with a 30-second TTL and measure the difference.
3. Use a sorted set to build a leaderboard with pagination.
4. Inspect `INFO memory` and explain `used_memory_peak`.

## Notes and limits

- This lab has no password. Add `--requirepass` and a private network before exposing Redis.
- `appendonly yes` enables the AOF persistence mode; data lives in the `redis-data` volume.
- Redis 8 includes query and vector features, but this lab sticks to the core data structures.
- Use `SCAN` rather than `KEYS` on any dataset that matters.

## Run it from anywhere

This lab publishes its ports on `127.0.0.1` only. To use it from another country, do **not** open the database port to the internet. Pick one:

- **VPS + private tunnel:** run the lab on a small Ubuntu VPS, keep the port closed, and connect through WireGuard or `ssh -L`.
- **Managed service:** use a managed free tier for this engine and point the same examples at its connection string.
- **HTTP UI only:** if the engine has a web UI, put it behind Caddy with TLS and basic auth.

The shared checklist, provider map, and commands are in **[REMOTE-ACCESS.md](https://github.com/devarent/database-labs/blob/main/REMOTE-ACCESS.md)**.

## Cleanup

```bash
docker compose down -v
```

`-v` also removes the named volume, so the next start is a clean slate.

## References

- [Redis documentation](https://redis.io/docs/latest/)
- [Redis commands](https://redis.io/docs/latest/commands/)
- [redis-py](https://redis-py.readthedocs.io/)

---

<sub>Part of the <a href="https://github.com/devarent/database-labs">database-labs</a> collection: 26 database engines, one index.</sub>

## License

MIT (c) 2026 Arya Fatthurahman. See [LICENSE](LICENSE).
