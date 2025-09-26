from App.database import db
from datetime import datetime, date, time
from App.models.shifts import Shifts
from App.models.staff import Staff


class Attendance (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    shift_id = db.Column(db.Integer, db.ForeignKey('shifts.id'))
    time_in = db.Column(db.String)
    time_out = db.Column(db.String)

    staff = db.relationship('Staff', backref= 'staff', lazy=True )


    def __init__(self, staff_id, shift_id, time_in, time_out=None):
      
        self.staff_id = staff_id
        self.shift_id = shift_id
        self.time_in = time_in
        self.time_out = time_out

    def get_json(self):
        return {
            "id": self.id,
            "staff_id": self.staff_id,
            "staff_name": self.staff.username,
            "shift_id": self.shift_id,
            "time_in": self.time_in,
            "time_out": self.time_out,
        }
    
    def __repr__(self):
        return f"<Attendance {self.id}: {self.staff.username} on Shift {self.shift_id}, In={self.time_in}, Out={self.time_out}>"