#!/usr/bin/python3

from csv_select import select_one_from_csv

csv = 'https://raw.githubusercontent.com/IrishMarineInstitute/uwobs/master/common/apps/adcp_config.csv'
query = '''
SELECT * FROM csv
         WHERE reference='adcp0'
         AND start_date<=datetime('now')
         AND end_date is null OR end_date >= datetime('now')
         ORDER BY start_date DESC LIMIT 1
         '''
answer = select_one_from_csv(csv,query)
print('# {}'.format(answer))
# prints this:
# {'index': 3, 'reference': 'adcp0', 'type': 'adcp', 'manufacturer': 'teledyne', 'id': 'TRDI-WHB600Hz-10488', 'moxa_server': '172.16.255.5', 'moxa_port': 952, 'start_date': '2019-05-03T10:00:00Z', 'end_date': None}
#
print ('''DEVICE={}
PORT={}
SERVER={}'''.format(answer['id'],answer['moxa_port'],answer['moxa_server']));

