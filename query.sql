-- кількість всіх призерів (за весь час) для кожного виду спорту
select sport , count( DISTINCT athlete.athlete_id) as winners
	from athlete, medal, sport 
		where athlete.athlete_id = medal.athlete_id 
			and medal.sport_id =sport.sport_id
	group by sport;


-- список країн і кількість отриманих медалей (за весь час)
select country, count(medal.medal_id) as medals
	from athlete, medal 
		where athlete.athlete_id = medal.athlete_id
	group by country
	order by medals desc;


-- всі роки олімпіад і кількість людей, що в них зайняли призові місця
select olympics.olymp_year as year, count( DISTINCT athlete.athlete_id) as winners
	from athlete, medal, olympics 
		where athlete.athlete_id = medal.athlete_id 
			and medal.olymp_year = olympics.olymp_year
	group by olympics.olymp_year;
