from abc import ABC, abstractmethod


class MyABC(ABC):
    @abstractmethod
    def say_hi(self):
        pass

    @abstractmethod
    def say_bye(self):
        pass


class User(MyABC):
    def say_hi(self):
        pass

    def say_bye(self):
        pass

user = User()
print(user)

