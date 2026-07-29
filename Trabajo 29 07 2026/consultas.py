import asyncpg
from fastapi import HTTPException
from loguru import logger

async def todos_los_autores(db: asyncpg.Connection):
    try:
        query = "SELECT * FROM autores;"
        rows = await db.fetch(query)
        return [dict(row) for row in rows]
    except Exception as e:
        logger.error("No se pudo consultar la base de datos")
        raise HTTPException(
            status_code=500, detail=f"Error en la base de datos: {str(e)}"
        )

async def autores_por_parametros(db: asyncpg.Connection, año_nacimiento: int, pais: str):
    try:
        query = "SELECT * FROM autores WHERE nacimiento = $1 AND pais = $2;"
        rows = await db.fetch(query, año_nacimiento, pais)
        return [dict(row) for row in rows]
    except Exception as e:
        logger.error("No se pudo consultar la base de datos")
        raise HTTPException(
            status_code=500, detail=f"Error en la base de datos: {str(e)}"
        )

async def obtener_autor_por_id(db: asyncpg.Connection, autor_id: int):
    try:
        query = "SELECT * FROM autores WHERE id = $1;"
        row = await db.fetchrow(query, autor_id)
        if row:
            return dict(row)
        return None
    except Exception as e:
        logger.error("No se pudo consultar la base de datos")
        raise HTTPException(
            status_code=500, detail=f"Error en la base de datos: {str(e)}"
        )