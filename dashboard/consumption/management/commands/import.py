from django.core.management.base import BaseCommand
from os.path import isfile, isdir
from consumption.models import User,Consumption
from django.utils.dateparse import parse_datetime
from django.utils.timezone import localtime
from decimal import Decimal

class Command(BaseCommand):
    """
    Imports csv files to database models user and consumption.
    Expects to find a file named user_data.csv, and a sub directory consumption/ 
    containing the consumption log files, names <user_id>.csv
    @param path: Path of data/ directory
    """
    help = """
        import customer data from CSV to django's database.
        
        usage: manage.py import <PATH>
        
        where path is the root directory containing user_data.csv 
        and a subdirectory consumption/ containing the consumption log CSVs
        """

    def add_arguments(self, parser):
        parser.add_argument('path',nargs='+',type=str); 

    def import_users(self,path):
        #Imports user_data.csv to model.User
        file_name=path+"/user_data.csv";
        print("Importing users in "+file_name+" this could take a while...");
        with open(file_name) as ud:
            contents=ud.readlines()[1:] #Skip header line
        for line in contents:
            user_id,area,tariff=line.strip().split(",")
            user=User(user_id=user_id,user_area=area,user_tariff=tariff)
            user.save()
            self.import_consumption(path,user)

    def import_consumption(self,path,user):
        #Imports consumption log csv for user
        uid=user.user_id
        full_path=path+"/consumption/"+uid+".csv"
        print(full_path)
        with open(full_path) as f:
            for line in f.readlines()[1:]:
                time_stamp,amount=line.strip().split(',')
                ts=parse_datetime(time_stamp +"+01:00") #TODO fix timezone (Always assumes UTC+1 , UK Time).
                consumption=Consumption(user=user,consumption_time=ts,consumption_amount=amount)
                consumption.save()

    def handle(self, *args, **options):
        path=options['path'][0]
        try:
            self.import_users(path)
        except IOError as e:
            print "IO Error, did you provide the correct path?"
            raise
        except:
            print("All errors in one pass, guess which one?")
            raise
