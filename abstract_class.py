from abc import ABC, abstractmethod
#In python to do abstraction you need to import ABC (that is the abstract base )
#"abstract method",this is a decorator and its used to add a meta information)

class User:
    first_name=""
    last_name=""
    user_id=78
    alias=""
    password=""
    email=""

class UserAbstract(ABC):
    @abstractmethod
    def create_user(self,user:User):
        pass
        
    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self,user_id):
        pass
#UserManager is a class derived from UserAbstract, this class you can instantiate
#when you instantiate an abstract class you must implement everything that was in it
class UseManager(UserAbstract):
    def create_user(self,user:User):
        print("user information")
        print("{first_name}")

    def get_all_users(self):
        print("hello tiny!we are getting users here")

    def get_user_by_id(self,user_id):
        print("hello world")

    # user_abs=UserAbstract
    #This can't be called because its and abstract class

    #Define all the class in the abstract class

user_manager=UseManager()
user_manager.get_all_users()

