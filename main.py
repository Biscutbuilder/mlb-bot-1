import statsapi
import datetime
from datetime import date
from mlbstatsapi import Mlb


with Mlb() as mlb:
    print(mlb.get_team(138))

team = mlb.get_team(138)
games = statsapi.schedule.team(date.today())

for game in games:
  x = datetime.datetime.now()
  print(
      f"{game['away_name']} ({game['away_score']}) @ {game['home_name']}"
      f" ({game['home_score']}) - {game['status']}"
      
      
  )
  
