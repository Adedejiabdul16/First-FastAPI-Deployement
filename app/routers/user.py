from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix = ('/users'),
    tags = ['Users']
)

@router.post('/', status_code = status.HTTP_201_CREATED, response_model = schemas.UserOut)
def create_users(user : schemas.UserCreate, db : Session = Depends(get_db)):
   
    hashed_pasword = utils.hash(user.password)
    user.password = hashed_pasword

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model =schemas.UserOut)
def get_user(id : int, db : Session = Depends(get_db)):
    get_user = db.query(models.User).filter(models.User.id == id)
    the_user = get_user.first()

    if not the_user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail =
                            f'the user with id : {id } does not exsit')
    
    return the_user