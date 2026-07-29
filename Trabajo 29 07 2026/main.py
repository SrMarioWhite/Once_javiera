from contextlib import asynccontextmanager
from typing import Annotated
from loguru import logger
import asyncpg
from fastapi import Depends, FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates


from consultas import todos_los_autores, autores_por_parametros, obtener_autor_por_id
from database import init_db_pool, close_db_pool, get_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestiona el ciclo de vida del pool de conexiones."""
    await init_db_pool()
    yield
    await close_db_pool()

app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")

@app.get("/autores")
async def listar_usuarios(
    db: asyncpg.Connection = Depends(get_db),
):
    """Endpoint concurrente para listar todos los autores."""
    datos = await todos_los_autores(db)
    return datos

@app.get("/autores1")
async def listar(
    request: Request,
    db: Annotated[asyncpg.Connection, Depends(get_db)],
    year: int | None = None,
    pais: str | None = None
):
    if year is None and pais is None:
        datos = await todos_los_autores(db)
    else:
        datos = await autores_por_parametros(db, year, pais)
    return datos

@app.get("/autores/id/{autor_id}")
async def obtener_un_autor(
    autor_id: int,
    db: Annotated[asyncpg.Connection, Depends(get_db)]
):
    """Obtiene un único autor por su ID."""
    datos = await obtener_autor_por_id(db, autor_id)
    if not datos:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return datos

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/autores/html")
async def listar_autores_html(
    request: Request,
    db: Annotated[asyncpg.Connection, Depends(get_db)],
    year: int | None = None,
    pais: str | None = None,
    autor_id: int | None = None,
):
    logger.info(f"Parametros recibidos: year={year}, pais={pais}, autor_id={autor_id}")
    
    if autor_id is not None:
        autor = await obtener_autor_por_id(db, autor_id)
        datos = [autor] if autor else []
        
    elif year is not None and pais is not None:
        # Consulta 2: Filtrar por año y país
        datos = await autores_por_parametros(db, year, pais)
        
    else:
        # Consulta 1: Todos los autores
        datos = await todos_los_autores(db)
        
    return templates.TemplateResponse(
        request=request, 
        name="respuesta.html", 
        context={"autores": datos}
    )