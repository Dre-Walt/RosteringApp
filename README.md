# RosteringApp
Assignment 1 COMP3613 Rostering App

A rostering and attendance management system built with Flask.  
This app allows **Admins** to schedule and manage shifts, while **Staff** can record attendance and view the combined roster.

---

## Features

### Admin
- Create staff schedules
- View all scheduled shifts
- Generate attendance/shift reports

### Staff
- Clock in to a shift
- Clock out of a shift
- View the combined roster

---

## CLI Commands

### Admin Commands
```bash
# Create a new shift for a staff member
#Date, starttime, endtime are strings
flask admin createsched <staff_id> <date> <start_time> <end_time>


# View all scheduled shifts
flask admin getshifts

# Generate a shift attendance report
flask admin report

### Staff Commands-----

# Record staff start of shift
flask staff clock_in <username> <shift_id>

# Record staff end of shift
flask staff clock_out <username> <shift_id>

# View combined roster
flask staff roster

### Database Initialization-----------------

# To clear and reinitialize the database (adds 2 admins and 4 staff)
flask init 

 create_admin('bob', 'bobpass')
 create_admin('susie', 'susie123')

 create_staff('ben', 'benpass')
 create_staff('jeff', 'jpass')
 create_staff('james', 'james123')
 create_staff('fred', 'fredpass')
