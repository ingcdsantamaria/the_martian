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