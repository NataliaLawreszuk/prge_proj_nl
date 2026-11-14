from fastapi import APIRouter


router_get_users = APIRouter()

@router_get_users.get("/users")
async def get_users():
    return [
        {'id': 1, 'name': 'Bartek'},
        {'id': 2, 'name': 'Emil'},
        {'id': 3, 'name': 'Mikołaj'},
        {'id': 4, 'name': 'Natalia'}
    ]