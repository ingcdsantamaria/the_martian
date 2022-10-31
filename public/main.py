#Imports
from datetime import date
import os
from urllib import response
from fastapi import FastAPI,Query,Path, HTTPException, status,Body, Request, Response, File,UploadFile, Form
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse, StreamingResponse, FileResponse

from pydantic import BaseModel, Field, AnyUrl
from typing import Optional, List, Dict

# DataBase
from database.database import desarrolladores, actores, personajes

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

class Personaje(BaseModel):
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
    return templates.TemplateResponse("./views/index.html", {"request": request, "actores": response,"title":"All actors"})


# Search a actor by ID
@app.post(
    path="/search",
    response_class=RedirectResponse,

)

def search_actor(id: str = Form(...)):
    return RedirectResponse("/actor/" + id, status_code=status.HTTP_302_FOUND)

#actor by id
@app.get(path="/actor/{id}",response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def get_actor_by_id(request: Request, id: int = Path(..., gt=0)):
    actor = actores.get(id)
    response = templates.TemplateResponse("search.html", {"request": request, "actor": actor, "id": id})
    if not actor:
        response.status_code = status.HTTP_404_NOT_FOUND
    return response



#list all personajes
@app.get(path="/character",response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def get_all_personajes(request: Request, number: Optional[str] = Query(default="5", max_length=3)):
    response = []
    for id, personaje in list(personajes.items())[:int(number)]:
        response.append((id,personaje))
    return templates.TemplateResponse("./views/character.html", {"request": request, "personajes": response})


#personaje by id
@app.get(path="/character/{id}",response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def get_personaje_by_id(request: Request, id: int = Path(..., gt=0, le=len(personajes))):
    personaje = personajes.get(id)
    response = templates.TemplateResponse("./views/searchCharacter.html", {"request": request, "personajes": personaje})
    if not personaje:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Personaje with id {id} not found")
    return response




#Ver imagen
@app.get(
    path="/show/image/{file_name}",
    status_code=status.HTTP_202_ACCEPTED
)
def show_image(
        file_name:str=Path(...)
):
    dir=directory_is_ready()
    path=dir+file_name
    return FileResponse(path)



#Manejo de archivos
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
    with open(f"static/{file.filename}", "wb") as mypicture:
        content = await file.read()
        mypicture.write(content)
        mypicture.close()
    return "Image saved successfully"

def directory_is_ready():
    os.makedirs(os.getcwd() + "/img", exist_ok=True)
    print(os.getcwd())
    return os.getcwd() + "/img"
