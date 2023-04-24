import aioredis

from complexity_app.settings import get_settings


settings = get_settings()

keydb_client = aioredis.from_url(settings.KEYDB_URL, password=settings.KEYDB_PASSWORD.get_secret_value())
