To import run:
$manage.py import <PATH>
for example
$./manage.py import ../data


Issue 1 - Time Zone.
the import process assumes UK time (UTC+1 hour), this should probably be determined by the user's area.

Issue 2 - Importing is long. 
can optimize code for faster importation. it's probably the database commits, be better off buffering all records and saving at once at the end instead of one by one as they are processed.

Issue 3 - Summary graph
The summary graph displays a graph, not I am not convinced it groups by days correctly, needs to check.

Issue 4 - Passing QuerySet to template 
passing the queryset directly to the template, ideally, we should format the data in the view, and pass as array. will probably also be quicker.


