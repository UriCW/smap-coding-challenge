Issue 1 - Time Zone.
the import process assumes UK time (UTC+1 hour), this should probably be determined by the user's area.

Issue 2 - Importing is long. can optimize code for faster importation. it's probably the daabase commits, be better off buffering all records and saving at once at the end instead of one by one as they are processed.

Issue 3 - The summary graph displays a graph, not I am not convinced it groups by days correctly, needs to check. also, I pass the queryset directly to the template, ideally, we should format the data in the view, and pass just the array. will probably also be quicker.

