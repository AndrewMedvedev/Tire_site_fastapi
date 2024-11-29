from fastapi import FastAPI
from routers.announcements import router as router_announcements
from routers.filters import router as router_filters

app = FastAPI()

app.include_router(router_announcements)
app.include_router(router_filters)
