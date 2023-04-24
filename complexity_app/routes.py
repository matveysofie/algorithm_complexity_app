import psutil as psutil
from datetime import datetime
from fastapi import Request, APIRouter

from complexity_app.schemas.responses import HealthcheckResponse
from complexity_app.services.keydb_client import keydb_client
from complexity_app.settings import get_settings

settings = get_settings()

router = APIRouter()


@router.get("/healthcheck", response_model=HealthcheckResponse)
async def healthcheck(request: Request):
    return {
        'uptime': (datetime.now() - datetime.fromtimestamp(psutil.boot_time())).total_seconds(),
        'keydb_is_alive': await keydb_client.ping()
            }
