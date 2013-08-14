import os, urlparse
DEBUG = True
REALM = os.environ.get('REALM', 'local')

ROOT_URL = "http://localhost:3000"

PORT_NUMBER = 4000

FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", "N1BKhJLnBqLpexOZdklsfDKFJDKFadsfs9a3r324YB7B73AglRmrHMDQ9RhXz35")

BIN_TTL = 48*3600
STORAGE_BACKEND = "requestbin.storage.redis.RedisStorage"
MAX_RAW_SIZE = 1024*10
IGNORE_HEADERS = []
MAX_REQUESTS = 20
CLEANUP_INTERVAL = 3600

REDIS_URL = ""
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_DB = 9
REDIS_PREFIX = "requestbin"

if REALM == 'prod':
    DEBUG = False
    ROOT_URL = "http://requestb.in"

    STORAGE_BACKEND = "requestbin.storage.redis.RedisStorage"

    REDIS_URL = os.environ.get("REDIS_URL")
    url_parts = urlparse.urlparse(REDIS_URL)
    REDIS_HOST = url_parts.hostname
    REDIS_PORT = url_parts.port
    REDIS_PASSWORD = url_parts.password
    REDIS_DB = url_parts.fragment

    IGNORE_HEADERS = """
X-Varnish
X-Forwarded-For
X-Heroku-Dynos-In-Use
X-Request-Start
X-Heroku-Queue-Wait-Time
X-Heroku-Queue-Depth
X-Real-Ip
X-Forwarded-Proto
X-Via
X-Forwarded-Port
""".split("\n")[1:-1]