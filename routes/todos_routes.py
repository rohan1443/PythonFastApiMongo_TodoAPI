from fastapi import APIRouter
from config.database import collection_name
from schemas.todos_shema import todo_serializer, todos_serializer
from models.todos_model import Todo
from bson import ObjectId

todo_api_router = APIRouter()


#retrive all data
@todo_api_router.get("/")
async def get_todos():
    todos = todos_serializer(collection_name.find())
    return {'status': 'ok', "data": todos}


#retrieve single data
@todo_api_router.get("/{id}")
async def get_todo(id: str):
    todo = todos_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {'status': 'ok', "data": todo}


#post a todo
@todo_api_router.post("/todo")
async def add_todo(todo: Todo):
    _id = collection_name.insert_one(dict(todo))
    todo = todos_serializer(collection_name.find({"_id": _id.inserted_id}))
    return {'status': 'ok', "data": todo}


#update a todo
@todo_api_router.put("/{id}")
async def update_todo(id: str, updated_todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)},
                                        {'$set': dict(updated_todo)})
    todo = todos_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": todo}


#delete a todo
@todo_api_router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}
