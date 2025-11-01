from abc import ABCMeta,abstractmethod
from user.domain.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_users(self, page:int, items_per_page:int) -> tuple[int,list[User]]:
        raise NotImplementedError
    
    @abstractmethod
    def get_users(self) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    def save(self,user:User):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_name(self,name:str):
        '''이름으로 유저 검색 뒤, 검색된 유저 없으면 에러 발생 시키기'''

        raise NotImplementedError

