from App.models import User, Staff, Admin, Shifts, Attendance
from App.models.attendance import Attendance
from App.database import db
from datetime import datetime

def schedule_shifts(staff_id, date, start_time, end_time):
    staff = Staff.query.get(staff_id)
    if not staff:
        return print(f'Staff member does not exist')
    
    shift= Shifts(staff_id=staff.id, date=date, start_time=start_time, end_time=end_time)
    db.session.add(shift)
    db.session.commit()
    return shift

def view_shift_report():
    return Attendance.query.all()
    