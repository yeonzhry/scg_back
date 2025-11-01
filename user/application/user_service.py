from dependency_injector.wiring import inject, Provide
from fastapi import Depends

from typing import Annotated
from datetime import datetime
from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.repository.user_repo import UserRepository
from fastapi import HTTPException, Depends
from ulid import ULID

class UserService:
    @inject
    def __init__(
        self,
        user_repo:IUserRepository,
    ):
        self.user_repo=user_repo

    def create_user(self,name:str):

        _user=None

        try:
            _user=self.user_repo.find_by_name(name)
        except HTTPException as e:
            if e.status_code !=422:
                raise e
        if _user:
            raise HTTPException(status_code=422)

        now=datetime.now()
        user:User=User(
            id=str(ULID()),
            name=name,
            created_at=now,
            updated_at=now,
        )
        self.user_repo.save(user)

        return user
    def get_users(self,page:int,items_per_page:int) -> tuple[int,list[User]]:
        users=self.user.get_users(page,items_per_page)

        return self.user_repo.get_users()

