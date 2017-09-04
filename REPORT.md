Issues
======

###### Issue 1 - Time Zone.

the import process assumes UK time (UTC+1 hour), this should probably be determined by the user's area.

###### Issue 2 - Importing is long. 

can optimize code for faster importation. it's probably the database commits, be better off buffering all records and saving at once at the end instead of one by one as they are processed.

###### Issue 3 - Summary graph

The summary graph displays a graph, not I am not convinced it groups by days correctly, needs to check.

###### Issue 4 - Passing QuerySet to template 

passing the queryset directly to the template, ideally, we should format the data in the view, and pass as array. will probably also be quicker.


Instructions
============
1. Clone this repository:
```bash
$cd /tmp
$git clone https://github.com/UriCW/smap-coding-challenge/
$cd smap-coding-challenge/
```
2. Create a virtualenv and install django
```bash
$mkdir venv
$virtualenv venv
$source venv/bin/activate
$pip install django
```

3. Initialise
```bash
$cd dashboard
$./manage.py makemigrations
$./manage.py migrate
```
4. Import CSV data
```bash
$./manage.py import ../data
```
  This will take a long time (as in hours). You can stop it after a few customers are done by using ctrl+c

5. Run server
```bash
$./manage.py runserver
```
6. Browse to http://localhost:8000

7. Hire me!
