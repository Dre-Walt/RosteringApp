from App.database import db
from datetime import datetime, date, time



class Shifts (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    staff_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.String(10), nullable=False)      
    start_time = db.Column(db.String(5), nullable=False) 
    end_time = db.Column(db.String(5), nullable=False) 

    staff= db.relationship("Staff", backref="shifts", lazy=True)
    attendances = db.relationship('Attendance', backref= 'shifts', cascade="all, delete-orphan", lazy=True)


    def __init__(self, staff_id, date, start_time, end_time):
        self.staff_id = staff_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"<Shift{self.id} staff_id={self.staff_id} name={self.staff.username} date={self.date} {self.start_time}-{self.end_time}>"

    def get_json_shifts(self):
        return {
            "id": self.id,
            "staff_id": self.staff_id,
            "staff_name": self.staff.username,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time
        }

