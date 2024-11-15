from typing import Optional
from pydantic import BaseModel


class ScrapeRequest(BaseModel):
    page_limit: int
    proxy_url: Optional[str] = None

    # NOTE: Additional fields can be added as needed
