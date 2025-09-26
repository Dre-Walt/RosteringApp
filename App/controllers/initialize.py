from .user import *
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
  
    create_admin('bob', 'bobpass')
    create_admin('susie', 'susie123')

    create_staff('ben', 'benpass')
    create_staff('jeff', 'jpass')
    create_staff('james', 'james123')
    create_staff('fred', 'fredpass')

