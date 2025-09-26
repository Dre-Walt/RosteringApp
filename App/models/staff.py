from App.models.user import User 
from App.database import db

class Staff(User):

    __mapper_args__ = {
        'polymorphic_identity' : 'staff'
    }

    def __init__(self, username, password):
        super().__init__(username, password)
        self.position = 'staff'

