import requests
import time
import json

url = "http://www.nfl.com/liveupdate/scores/scores.json"

json_data = requests.get(url).json()

for key, value in json_data.items():
#    game = key
#    print('Game ID: ' + game)
    home_team = value['home']['abbr']
    home_score = value['home']['score']['T']
    away_team = value['away']['abbr']
    away_score = value['away']['score']['T']
    poss_team = value['posteam']
    quarter = value['qtr']
    ball_on = value['yl']
    down = value['down']
    to_go = value['togo']
    clock = value['clock']
    print('AWAY: ' + away_team + ' : ' + str(away_score))
    print('HOME: ' + home_team + ' : ' + str(home_score))
    if quarter == None:
	print('--------------------')
    else:
	if quarter == "Final":
		print('QTR: ' + str(quarter))
		print('--------------------')
	else:
		if quarter == "Pregame":
			print('QTR: ' + str(quarter))
			print('--------------------')
		else:
			if quarter == "Halftime":
				print('QTR: ' + str(quarter))
				print('--------------------')
			else:
				print('QTR: ' + str(quarter) + " | " + str(clock))
				print(str(poss_team) + ' POSS')
				print(str(down) + ' & ' + str(to_go) + ' on the ' + str(ball_on))
				print('--------------------')
    time.sleep(5)

    
    

    
#    for sub_key,sub_value in value.items():
#        print(sub_key, sub_value)

#game = json_data['2018082651']
#home_team = game['home']['abbr']
#home_score = game['home']['score']['T']
#away_team = game['away']['abbr']
#away_score = game['away']['score']['T']
#print('AWAY: ' + away_team + ' : ' + str(away_score))
#print('HOME: ' + home_team + ' : ' + str(home_score))
#    print('--------')
