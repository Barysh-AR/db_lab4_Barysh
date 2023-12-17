INSERT INTO Olympics(Olymp_year, city)
VALUES
(2004,'Athens'),
(2012,'London');

INSERT INTO Athlete(Athlete_name, country, gender, Athlete_id)
VALUES
('MANAUDOU, Laure', 'FRA', 'Women', 1),
('COUGHLIN, Natalie', 'USA', 'Women', 2),
('COVENTRY, Kirsty', 'ZIM', 'Women', 3),
('DE BRUIJN, Inge', 'NED', 'Women', 4),
('THOMAS, Petria', 'AUS', 'Women', 5),
('JEDRZEJCZAK, Otylia', 'POL', 'Women', 6),
('KUTSCHER, Marco', 'GER', 'Men', 7),
('PESSOA, Rodrigo', 'BRA', 'Men', 8),
('KAPPLER, Chris', 'USA', 'Men', 9),
('GUERDAT, Steve', 'SUI', 'Men', 10),
('SCHRODER, Gerco', 'NED', 'Men', 11),
('OCONNOR, Cian', 'IRL', 'Men', 12),
('JIN, Jongoh', 'KOR', 'Men', 13),
('TESCONI, Luca', 'ITA', 'Men', 14),
('ZLATIC, Andrija', 'SRB', 'Men', 15);

INSERT INTO Sport(Sport, discipline, sport_event, sport_id)
VALUES
('Aquatics', 'Swimming', '100M Backstroke', 1),
('Aquatics', 'Swimming', '100M Butterfly', 2),
('Equestrian', 'Jumping', 'Individual', 3),
('Shooting', 'Shooting', '10M Air Pistol', 4);

INSERT INTO Medal (medal_type, medal_id, sport_id, olymp_year, athlete_id)
VALUES
('Bronze', 1,  1, 2004, 1),
('Gold',   2,  1, 2004, 2),
('Silver', 3,  1, 2004, 3),
('Bronze', 4,  2, 2004, 4),
('Gold',   5,  2, 2004, 5),
('Silver', 6,  2, 2004, 6),
('Bronze', 7,  3, 2004, 7),
('Gold',   8,  3, 2004, 8),
('Silver', 9,  3, 2004, 9),
('Gold',   10, 3, 2012, 10),
('Silver', 11, 3, 2012, 11),
('Bronze', 12, 3, 2012, 12),
('Gold',   13, 4, 2012, 13),
('Silver', 14, 4, 2012, 14),
('Bronze', 15, 4, 2012, 15);
