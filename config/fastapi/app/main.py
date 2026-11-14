from fastapi import FastAPI
#Importujemy klasę FastAPI z zainstalowanej biblioteki fastapi.
from app.routes.static_content import router_get_users
from app.routes.dynamic_content import router_get_users_from_database

app = FastAPI()
#Tworzymy obiekt aplikacji FastAPI i przypisujemy go do zmiennej app.

app.include_router(router_get_users, prefix="/app")
app.include_router(router_get_users_from_database, prefix="/app")

