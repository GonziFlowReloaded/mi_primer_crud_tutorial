from fastapi import APIRouter, HTTPException
from models.models import TareaRequest, TareaResponse
from core.mongo import mongo_db
from bson import ObjectId

router = APIRouter(prefix="/tareas", tags=["Tareas"])

@router.post("/", response_model=TareaResponse)
def create_tarea(tarea: TareaRequest):
    """
    Crea una nueva tarea.

    Args:
        tarea (TareaRequest): Objeto con los datos de la tarea a crear.

    Returns:
        TareaResponse: Objeto con los datos de la tarea creada, incluyendo su ID.
    """
    tarea_dict = tarea.dict()
    result = mongo_db.insert_one("tareas", tarea_dict)
    tarea_dict["id"] = str(result.inserted_id)
    return TareaResponse(**tarea_dict)

@router.get("/{tarea_id}", response_model=TareaResponse)
def get_tarea(tarea_id: str):
    """
    Obtiene una tarea por su ID.

    Args:
        tarea_id (str): ID de la tarea a buscar.

    Returns:
        TareaResponse: Objeto con los datos de la tarea encontrada.

    Raises:
        HTTPException: Si no se encuentra la tarea.
    """
    tarea = mongo_db.find_one("tareas", {"_id": ObjectId(tarea_id)})
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea not found")
    tarea["id"] = str(tarea["_id"])
    del tarea["_id"]
    return TareaResponse(**tarea)

@router.put("/{tarea_id}", response_model=TareaResponse)
def update_tarea(tarea_id: str, tarea: TareaRequest):
    """
    Actualiza una tarea existente.

    Args:
        tarea_id (str): ID de la tarea a actualizar.
        tarea (TareaRequest): Objeto con los nuevos datos de la tarea.

    Returns:
        TareaResponse: Objeto con los datos actualizados de la tarea.

    Raises:
        HTTPException: Si no se encuentra la tarea.
    """
    tarea_dict = tarea.dict()
    result = mongo_db.update_one("tareas", {"_id": ObjectId(tarea_id)}, {"$set": tarea_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Tarea not found")
    tarea_dict["id"] = tarea_id
    return TareaResponse(**tarea_dict)

@router.delete("/{tarea_id}")
def delete_tarea(tarea_id: str):
    """
    Elimina una tarea por su ID.

    Args:
        tarea_id (str): ID de la tarea a eliminar.

    Returns:
        dict: Mensaje de confirmación de eliminación.

    Raises:
        HTTPException: Si no se encuentra la tarea.
    """
    result = mongo_db.delete_one("tareas", {"_id": ObjectId(tarea_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Tarea not found")
    return {"message": "Tarea deleted successfully"}

@router.get("/", response_model=list[TareaResponse])
def list_tareas():
    """
    Lista todas las tareas existentes.

    Returns:
        list[TareaResponse]: Lista de objetos con los datos de todas las tareas.
    """
    tareas = mongo_db.find_all("tareas")
    for tarea in tareas:
        tarea["id"] = str(tarea["_id"])
        del tarea["_id"]
    return [TareaResponse(**tarea) for tarea in tareas]
