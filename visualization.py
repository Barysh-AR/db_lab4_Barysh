import psycopg2
import matplotlib.pyplot as plt

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

with conn:

    cur = conn.cursor()



    cur.execute(query_1)
    sport = []
    winners = []
    for row in cur:
        sport.append(row[0])
        winners.append(row[1])

    x_range = range(len(sport))
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, winners, label='Total')
    bar_ax.bar_label(bar, label_type='center')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(sport)
    bar_ax.set_xlabel('Вид спорту')
    bar_ax.set_ylabel('Кількість переможців')
    bar_ax.set_title('Кількість переможців,\nякі брали участь в певному виді спорту')



    cur.execute(query_2)
    country = []
    medals = []
    for row in cur:
        country.append(row[0])
        medals.append(row[1])

    pie_ax.pie(medals, labels=country, autopct='%1.1f%%')
    pie_ax.set_title('Частка країн\nсеред отриманих нагород')



    cur.execute(query_3)
    year = []
    winners = []
    for row in cur:
        year.append(row[0])
        winners.append(row[1])

    mark_color = 'blue'
    graph_ax.plot(year, winners, color=mark_color, marker='o')
    for qnt, price in zip(year, winners):
        graph_ax.annotate(price, xy=(qnt, price), color=mark_color, xytext=(7, 2), textcoords='offset points')    
    graph_ax.set_xlabel('Рік проведення')
    graph_ax.set_ylabel('Переможці')
    graph_ax.set_title('Графік залежності кількості переможців \nвід року проведення олімпіади\n(серед данних лише 2 роки)')


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()