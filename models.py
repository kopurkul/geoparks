from pydantic import BaseModel, UUID4
from typing_extensions import List


class User(BaseModel):
    id: int
    username: str
    password: str
    role: str


class TokenData(BaseModel):
    username: str | None = None


class ChangePictures(BaseModel):
    id: int
    old_name: str
    new_name: str


class DeletePicture(BaseModel):
    id: int
    picture_name: str


class LoginResponce(BaseModel):
    token: str


class GeoparkModel(BaseModel):
    id: UUID4
    name: str
    description: str
    latitude: float
    longitude: float


class GeoobjectModel(BaseModel):
    id: UUID4
    name: str
    description: str
    longitude: float
    latitude: float
    type: str
    geoparkId: str


class GeoobjectModelDetail(BaseModel):
    id: UUID4
    name: str
    description: str
    longitude: float
    latitude: float
    type: str
    geoparkId: str
    photoPaths: List[str]


class PhotoModel(BaseModel):
    id: UUID4
    path: str
    geoobjectId: UUID4
    preview: bool


class PathModel(BaseModel):
    path: str


class UpdateGeoobjectModel(BaseModel):
    name: str | None = None
    description: str | None = None
    longitude: float | None = None
    latitude: float | None = None
    type: str | None = None
    geoparkId: str | None = None