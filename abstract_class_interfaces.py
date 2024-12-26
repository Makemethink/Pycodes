from abc import ABC, abstractmethod
from dataclasses import dataclass

# Interface : Contains only abstract method
# Abstract Class : Contains abstract method and implementation (a concrete method)

@dataclass
class Course(ABC):
    """
        Interface because it also contains welcome_message implementation (a concrete class)
    """
    @classmethod
    @abstractmethod
    def list_course(cls) -> None:
        pass

    @staticmethod
    def welcome_message() -> str:
        return 'Hello user, it\'s nice to see you here'

@dataclass
class AbstractClass(ABC):
    """
        Abstract class because it only contains the abstract method not single implementation
    """
    @classmethod
    @abstractmethod
    def list_course(cls) -> None:
        pass

    @staticmethod
    @abstractmethod
    def welcome_message() -> None:
        pass
