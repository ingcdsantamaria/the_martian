
from datetime import date

#funcion para calcular la edad de un actor tomando la variable born_date del modelo Actor
def calculate_age(born_date):
    today = date.today()
    return today.year - born_date.year - ((today.month, today.day) < (born_date.month, born_date.day))

desarrolladores={
    "cristhian":{
        'name': 'Cristian David',
        'lastName': 'Santamaria Leon',
        'picture': '../static/images/desarrollador_cristhianS.png',
        'age': 23,
        'profession': 'Desarrollador de Software marciano',
        'description': 'Estudiante de Ingenieria de Sistemas y Computacion de la Universidad catolica de Colombia que se dedica a viajar por los diferentes soles del universo',
        'email': 'cdsantamaria28@ucatolica.edu.co',
        'gitlab': 'https://gitlab.com/cdsantamaria28',
        'phone': 3134097747,
    },
    "daniel":{
        'name': 'Daniel Josue',
        'lastName': 'Valderrama Leon',
        'picture': '../static/images/desarrollador_danielV.png',
        'age': 20,
        'profession': 'Ingeriero marciano de aliens sistematicos y computos galacticos',
        'description': 'Estudiante de Ingenieria marciana de aliens sistematicos y computos de la Universidad galactica catolica de Colombia dedicado a estudiar las estrellas y sus funciones en los marcianos',
        'email': 'djvalderrama67@ucatolica.edu.co',
        'gitlab': 'https://gitlab.com/djvalderrama67',
        'phone': 3204341780,
    },
    "cristian":{
        'name': 'Cristian ',
        'lastName': 'Aldebo Fernandez',
        'picture': '../static/images/desarrollador_cristianA.png',
        'age': 40,
        'profession': 'Constructor de mundos',
        'description': 'Creador de mundos y ejecutivo comercial de nuevas galaxias',
        'email': 'caldebo35@ucatolica.edu.co',
        'gitlab': 'https://gitlab.com/krisalde',
        'phone': 3163629133,
    }
}


actores={
    1:{
        'first_name': 'Kate',
        'last_name': 'Mara',
        'picture': '../static/images/Actor_Kate_Mara.png',
        'born_date': date(1983, 2, 27),
        'shows_age': calculate_age(date(1983, 2, 27)),
        'awards': 'nominada a los Premios Primetime Emmy en 2014 por su papel de Zoe Barnes en House of Cards',
        'movies': 'Transsiberian, Big Guy,The open Roads,Entourage,DeadFall,House of Cars,Trascendence4, Fantasticos,The Martian',
        'web': 'https://es.wikipedia.org/wiki/Kate_Mara',
        'instagram': 'https://www.instagram.com/katemara/?hl=es',
    },
    2:{
        'first_name': 'Aksel',
        'last_name': 'Hennie',
        'picture': '../static/images/Actor_Aksel_Hennie.png',
        'born_date': date(1975, 10, 29),
        'shows_age': calculate_age(date(1975, 10, 29)),
        'awards': 'Gano en 2009 premio al mejor actor por Max Manus: Man of war',
        'movies': '90 Minutes (2012),Pion??r (2013),H??rcules (2014),Last Knights (2015),The Martian (2015)',
        'web': 'https://es.wikipedia.org/wiki/Aksel_Hennie',
        'instagram': 'https://www.instagram.com/akselhennie/?hl=es',
    },
    3:{
        'first_name': 'Sebastian',
        'last_name': 'Stan',
        'picture': '../static/images/Actor_Sebastian_Stan.pmg.png',
        'born_date': date(1982, 9, 13),
        'shows_age': calculate_age(date(1982, 9, 13)),
        'awards': 'Nominado a mejor actor en 2013, 2015, 2016,Ganador en 2017, 2021',
        'movies': 'Captain America: The Winter Soldier,Ant-Man, The Bronze, Ricki and the Flash, The Martian',
        'web': 'https://es.wikipedia.org/wiki/Sebastian_Stan',
        'instagram': 'https://www.instagram.com/imsebastianstan/?hl=es',
    },
    4:{
        'first_name': 'Chiwetel',
        'last_name': 'Ejiofor',
        'picture': '../static/images/Actor_Chiwetel_Ejiofor.png',
        'born_date': date(1977, 7, 10),
        'shows_age': calculate_age(date(1977, 7, 10)),
        'awards': 'Nominado como mejor actor en 2013, nominado a los globos de oro en en 2006 y 2013, Ganador de los premios BAFTA 2013, nominado al premio del sindicato de actores 2008 y 2013',
        'movies': 'El ni??o que dom?? el viento, Maleficent: Mistress of Evil	Conall, The Old Guard, Infinite, Doctor Strange in the Multiverse of Madness, The Martian',
        'web': 'https://es.wikipedia.org/wiki/Chiwetel_Ejiofor',
        'instagram': 'https://www.instagram.com/chiwetelejiofor__/?hl=es',
    },
    5:{
        'first_name': 'Sean',
        'last_name': 'Bean',
        'picture': '../static/images/Actor_Sean_Bean.png',
        'born_date': date(1959, 4, 17),
        'shows_age': calculate_age(date(1959, 4, 17)),
        'awards': '"Premios Emmy - Mejor actor 2013 Accused, Premios SAG - Mejor reparto 2003 El Se??or de los Anillos: el retorno del Rey, Distinciones  -  Premio de la Cr??tica Cinematogr??fica al mejor reparto (2003)"',
        'movies': 'El se??or de los anillos,Troya, GoldenEye, Terror en Silent Hill, La leyenda del tesoro perdido, The Hitcher, The Martian',
        'web': 'https://es.wikipedia.org/wiki/Sean_Bean',
        'instagram': 'https://www.instagram.com/sean_bean_official/?hl=es',
    },
    6:{
        'first_name': 'Benedict',
        'last_name': 'Wrong',
        'picture': '../static/images/Actor_Benedict_Wong.png',
        'born_date': date(1971, 7, 3),
        'shows_age': calculate_age(date(1971, 7, 3)),
        'awards': 'Premio al mejor actor de reparto de Hong Kong en los 24th Hong Kong Film Awards y en los 10th Golden Bauhinia Awards',
        'movies': 'Doctor Strange en el Multiverso de la Locura, Shang-Chi y la leyenda de los Diez Anillos, Marco Polo, She-Hulk, Raya y el ??ltimo, The Martian',
        'web': 'https://es.wikipedia.org/wiki/Benedict_Wong',
        'instagram': 'https://www.instagram.com/wongrel/?hl=es',
    },
    7:{
        'first_name': 'Matt',
        'last_name': 'Damon',
        'picture': '../static/images/Actor_Matt_Damon.png',
        'born_date': date(1970, 10, 8) ,
        'shows_age': calculate_age(date(1970, 10, 8)),
        'awards': 'Nominado como mejor actor y gan?? el galard??n al mejor guion original por Good Will Hunting ---nominado en 2010 como mejor actor de reparto por Invictus ---Nominado como mejor actor en 2016 por The Martian --- Nominaci??n en 2017 en la categor??a de mejor pel??cula por haber producido Manchester by the Sea --n los Globos de Oro, ha sido nominado en siete ocasiones, de las cuales ha ganado dos; mejor guion por Good Will Hunting y mejor actor de comedia o musical por The Martian.',
        'web': 'https://es.wikipedia.org/wiki/Matt_Damon',
        'instagram': 'https://www.instagram.com/mattdamonteam/?hl=es',
    },
    8:{
        'first_name': 'Jessica',
        'last_name': 'Chastein',
        'picture': '../static/images/Actor_Jessica_Chastain.png',
        'born_date': date(1977, 3, 24),
        'shows_age': calculate_age(date(1977, 3, 24)),
        'awards': 'Premio ??scar en la categor??a de Mejor Actriz, nominada a: Mejor Actriz de Reparto por The Help y Mejor Actriz por Zero Dark Thirty. Gan?? el Globo de Oro a la mejor actriz - Drama por Zero Dark Thirty, nominada seis veces m??s por sus trabajos en papeles protagonistas como en: Miss Sloane, Molly Game y The Eyes of Tammy Faye; En papeles secundarios como en: The Help y A Most Violent Year',
        'movies': 'Jolen Stolen The Debt The Tree of live Texas Killing Fields Coriolanus Take Shalter The help Lawless Madagascar 3 The color of time La noche mas oscura Mam?? Salom?? Miss Juli?? Interestellar A most violent year Unity La cumbre escarlata The Martian The Huntsman Miss Sloane I am Jane Doe Molly game Woman Walks Ahead Darl Phoenix It: Capitulo 2 AVA Agentes 335',
        'web': 'https://es.wikipedia.org/wiki/Jessica_Chastain',
        'instagram': 'https://www.instagram.com/jessicachastain/?hl=es',
    },
    9:{
        'first_name': 'Michael',
        'last_name': 'Pe??a',
        'picture': '../static/images/Actor_Michael_Pena.png',
        'born_date': date(1976, 1, 13),
        'shows_age': calculate_age(date(1976, 1, 13)),
        'awards': 'Premio del Sindicato de Actores al mejor actor de reparto, Alma Aword Actor favorito, Alma Aword Actor de serie favorito',
        'movies': '2010: Everything Must Go, como Frank Garc??a. 2011: El buen doctor, como Jimmy. 2011: Battle: Los Angeles, como Joe Rinc??n. 2011: The Lincoln Lawyer, como Jes??s Mart??nez. 2011: 30 Minutes or Less, como Chango. 2011: Tower Heist, como Enrique Dev Reaux. 2012: Chavez: Fight in the Field, como C??sar Ch??vez. 2012: End of Watch, como Mike Zavala. ',
        'web': 'https://es.wikipedia.org/wiki/Michael_Pe%C3%B1a',
        'instagram': 'https://www.instagram.com/mvegapena/?hl=es',
    },
}


characters={
    1:{
        'name': 'Beth',
        'lastname': 'Johanssen',
        'profession': 'Especialista en inform??tica',
        'role': 'especialista en inform??tica',
        'days_out_of_earth': 6,
        'shows_actor': 1,
    },
    2:{
        'name': 'Alex',
        'lastname': 'Vogel',
        'profession': 'Astroqu??mico del Ares 3',
        'role': 'Astroqu??mico del Ares 3',
        'days_out_of_earth': 6,
        'shows_actor': 2,
    },
    3:{
        'name': 'Dr. Chris',
        'lastname': 'Beck',
        'profession': 'Cirujano de vuelo y especialista en EVA',
        'role': 'Cirujano de vuelo y especialista en EVA',
        'days_out_of_earth': 6,
        'shows_actor': 3,
    },
    4:{
        'name': 'Venkat',
        'lastname': 'Kapoor',
        'profession': 'Director del programa ??res',
        'role': 'Director del programa ??res',
        'days_out_of_earth': 0,
        'shows_actor': 4,
    },
    5:{
        'name': 'Mitch',
        'lastname': 'Henderson',
        'profession': 'Jefe de cuerpo de Astronautas',
        'role': 'Jefe de cuerpo de Astronautas',
        'days_out_of_earth': 0,
        'shows_actor': 5,
    },
    6:{
        'name': 'Bruce',
        'lastname': 'Ng',
        'profession': 'Director de JPL',
        'role': 'Director de JPL',
        'days_out_of_earth': 0,
        'shows_actor': 6,   
    },
    7:{
        'name': 'Mark',
        'lastname': 'Watney',
        'profession': 'Astrobot??nico e ingeniero',
        'role': 'Astrobotanico e ingeniero',
        'days_out_of_earth': 561,
        'shows_actor': 7,   
    },
    8:{
        'name': 'Melissa',
        'lastname': 'Lewis',
        'profession': 'Comandante del Ares',
        'role': 'Comandante del Ares',
        'days_out_of_earth': 6,
        'shows_actor': 8,
    },
    9:{
        'name': 'Rick',
        'lastname': 'Martinez',
        'profession': 'Piloto del Ares 3',
        'role': 'Piloto del Ares 3',
        'days_out_of_earth': 6,
        'shows_actor': 9,
    }
}