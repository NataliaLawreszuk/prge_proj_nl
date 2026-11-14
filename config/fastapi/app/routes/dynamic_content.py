from difflib import diff_bytes

from fastapi import APIRouter
from sqlalchemy import create_engine, text
import os

db_name=os.getenv('PSTGRES_DB')
db_user=os.getenv('POSTGRES_USER')
db_password=os.getenv('POSTGRES_PASSWORD')

router_get_users_from_database = APIRouter()

@router_get_users_from_database.get("/users_db")
async def get_users():
    try:
        db_connection = create_engine(f'postgresql://{db_user}: {db_password}@postgis:5432/{db_name}')
        sql_query = f'select * from public.users;'

        with db_connection.connect() as connection:
            result = connection.execute(text(sql_query)).fetchall()
            users = [dict(row._mapping) for row in result]
        return users
    except Exception as e:
        print('error')
        return {'error': str(e)}