#Imports
from datetime import date
from importlib.resources import path
import os
from urllib import request, response
from fastapi import FastAPI,Query,Path, HTTPException, status,Body, Request, Response, File,UploadFile, Form
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse, StreamingResponse, FileResponse

from pydantic import BaseModel, Field, AnyUrl
from typing import Optional, List, Dict


# DataBase
from database.database import desarrolladores, actores, characters


class Desarrollador(BaseModel):
    name: Optional[str]
    lastName: Optional[str]
    picture: Optional[str]
    age: Optional[int]
    profession: Optional[str]
    descripstion: Optional[str]
    email: Optional[str]
    gitlab: Optional[AnyUrl]
    phone: Optional[int]

class Actor(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    picture: Optional[str]
    born_date: Optional[date]
    shows_age: Optional[int]
    awards: Optional[List[str]]
    movies: Optional[List[str]]
    web: Optional[AnyUrl]
    instagram: Optional[AnyUrl]

class character(BaseModel):
    name: Optional[str]
    lastname: Optional[str]
    profession: Optional[str]
    role: Optional[str]
    days_out_of_earth: Optional[int]
    shows_actor: Optional[int]






app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# Home
@app.get("/",response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("./views/home.html", {"request": request})

#list all desarrolladores
@app.get(path="/about",response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def get_all_desarrolladores(request: Request, number: Optional[str] = Query(default="5", max_length=3)):
    response = []
    for id, desarrollador in list(desarrolladores.items())[:int(number)]:
        response.append((id,desarrollador))
    return templates.TemplateResponse("./views/about.html", {"request": request, "desarrolladores": response})


#list all actores
@app.get(path="/actor",response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def get_all_actores(request: Request, number: Optional[str] = Query(default="5", max_length=3)):
    response = []
    for id, actor in list(actores.items())[:int(number)]:
        response.append((id,actor))
    return templates.TemplateResponse("./views/index.html", {"request": request, "actores": response,"title":"All actors", "path": request.url.path.split('/')[1]})



#actor by id
@app.get(path="/actor/{id}",response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def get_actor_by_id(request: Request, id: int = Path(..., gt=0)):
    actor = actores.get(id)
    response = templates.TemplateResponse("search.html", {"request": request, "actor": actor, "id": id, "path": request.url.path.split('/')[1]})
    if not actor:
        response.status_code = status.HTTP_404_NOT_FOUND
    return response



#list all characters
@app.get(path="/character",response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def get_all_characters(request: Request, number: Optional[str] = Query(default="5", max_length=3)):
    response = []
    for id, character in list(characters.items())[:int(number)]:
        response.append((id,character))
    return templates.TemplateResponse("./views/character.html", {"request": request, "characters": response, "path": request.url.path.split('/')[1]})


#character by id
@app.get(path="/character/{id}",response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def get_character_by_id(request: Request, id: int = Path(..., gt=0)):
    character = characters.get(id)
    response = templates.TemplateResponse("search.html", {"request": request, "character": character, "id": id, "path": request.url.path.split('/')[1]})
    if not character:
        response.status_code = status.HTTP_404_NOT_FOUND
    return response


# Search a actor by ID
@app.post(
    path="/search/{path}",
    response_class=RedirectResponse,

)
def search_actor_or_character(request: Request,id: str = Form(...), path: str =Path(...)):
    print(request.url)
    return RedirectResponse("/" + path + "/" + id, status_code=status.HTTP_302_FOUND)





#Ver imagen
@app.get(
    path="/static/images/{file_name}",
    status_code=status.HTTP_202_ACCEPTED
)
def show_image(
        file_name:str=Path(...)
):
    dir=directory_is_ready()
    path=dir+file_name
    return FileResponse(path)



#ver Manejo de archivos o type
@app.post(path="/post/image",status_code=status.HTTP_202_ACCEPTED)
def post_image(
        image:UploadFile=File(...)
):
    return { "Nombre del Archivo": image.filename,
        "Formato": image.content_type,
        "Tamaño": len(image.file.read())
    }

# upload image
@app.post("/upload", status_code=status.HTTP_201_CREATED)
#async
async def upload_image(file: UploadFile = File(...)):
    with open(f"static/images/{file.filename}", "wb") as mypicture:
        content = await file.read()
        mypicture.write(content)
        mypicture.close()
    return "Image saved successfully"

def directory_is_ready():
    os.makedirs(os.getcwd() + "/img", exist_ok=True)
    print(os.getcwd())
    return os.getcwd() + "/img"