from dependency_injector.wiring import inject, Provide
from containers import Container
from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from user.application.user_service import UserService

router=APIRouter(prefix="/users")

class CreateUserBody(BaseModel):
    name:str

@router.post("",status_code=201,response_model=None)
def create_user(
    user:CreateUserBody,
    user_service: UserService,
    use
):
    created_user=user_service.create_user(
        name=user.name
    )

    return created_user

@router.get("",response_model=None)
@inject
def get_users(
    user_service: UserService,
    page: int=1,
    items_per_page:int=10,
):
    total_count, users=user_service.get_users(page, items_per_page)

    return {
        "total_count":total_count,
        "page":page,
        "users":users,
    }
    