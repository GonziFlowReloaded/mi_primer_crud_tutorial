from pydantic import BaseModel
from typing import List

class TareaRequest(BaseModel):
    titulo: str
    descripcion: str
    fecha_inicio: str
    fecha_fin: str
    estado: str

class TareaResponse(BaseModel):
    id: str
    titulo: str
    descripcion: str
    fecha_inicio: str
    fecha_fin: str
    estado: str