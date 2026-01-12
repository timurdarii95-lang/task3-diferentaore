from calendar import different_locale
from datetime import datetime
from zoneinfo  import ZoneInfo

start_time = input("Introdu start_datetime YYYY-MM-DD, HH-MM-SS: ")
end_time = input("Introdu end_datatime YYYY-MM-DD, HH-MM-SS: ")

format_time = '%Y-%m-%d, %H-%M-%S'

t1 = datetime.strptime(start_time, '%Y-%m-%d, %H-%M-%S')
t2 = datetime.strptime(end_time, '%Y-%m-%d, %H-%M-%S')

dif = t2 - t1

ore = dif.total_seconds() / 3600
print(f'Diferenta dintre cele doua date este de {ore}ore.')
