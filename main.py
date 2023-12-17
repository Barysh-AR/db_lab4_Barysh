import psycopg2

username = 'Artem_Barysh'
password = '123'
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_1 = '''
select sport , count( DISTINCT athlete.athlete_id) as winners
	from athlete, medal, sport 
		where athlete.athlete_id = medal.athlete_id 
			and medal.sport_id =sport.sport_id
	group by sport;
'''
query_2 = '''
select country, count(medal.medal_id) as medals
	from athlete, medal 
		where athlete.athlete_id = medal.athlete_id
	group by country
	order by medals desc;
'''
query_3 = '''
select olympics.olymp_year as year, count( DISTINCT athlete.athlete_id) as winners
	from athlete, medal, olympics 
		where athlete.athlete_id = medal.athlete_id 
			and medal.olymp_year = olympics.olymp_year
	group by olympics.olymp_year;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
                       
    print ("Database opened successfully")
    
    cur = conn.cursor()


    print('\n1. ')
    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\n2. ')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\n3. ')
    cur.execute(query_3)
    for row in cur:
        print(row)