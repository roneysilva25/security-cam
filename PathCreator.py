import os 
from datetime import date, datetime

class PathCreator:
    def __init__(self) -> None:
        pass
    
    def getPath(self):
        months = ['JAN', 'FEV', 'MARC', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
        now_info = datetime.now()
        filename = "-".join(str(now_info)[:-7].split(":"))
        filename = filename.split(" ")[1]
        year = now_info.year
        monthindex = now_info.month
        dataCompleta = date.today()
        wd = os.getcwd()
        wd = '/'.join(wd.split("\\"))
        path = f'/{year}/{months[monthindex-1]}/{dataCompleta}/'
        try:
            os.makedirs(path)
        except FileExistsError:
            pass
        return path + filename
