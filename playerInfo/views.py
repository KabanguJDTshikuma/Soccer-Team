from django.shortcuts import render
import http.client
import json



def playerInfo(request):
    teams_id = {'Arsenal FC': 57, 'Aston Villa FC': 58, 'Blackburn Rovers FC': 59, 'Bolton Wanderers FC': 60,
                 'Chelsea FC': 61, 'Everton FC': 62, 'Fulham FC': 63, 'Liverpool FC': 64, 
                 'Manchester City FC': 65, 'Manchester United FC': 66, 'Newcastle United FC': 67, 
                 'Norwich City FC': 68, 'Queens Park Rangers FC': 69, 'Stoke City FC': 70, 'Sunderland AFC': 71,
                  'Tottenham Hotspur FC': 73, 'West Bromwich Albion FC': 74, 'Wigan Athletic FC': 75,
                   'Wolverhampton Wanderers FC': 76, 'Hull City AFC': 322, 'Burnley FC': 328, 
                   'Birmingham City FC': 332, 'Leicester City FC': 338, 'Southampton FC': 340, 
                   'Leeds United AFC': 341, 'Derby County FC': 342, 'Middlesbrough FC': 343, 
                   'Sheffield Wednesday FC': 345, 'Watford FC': 346, 'Ipswich Town FC': 349, 
                   'Nottingham Forest FC': 351, 'Crystal Palace FC': 354, 'Reading FC': 355, 
                   'Sheffield United FC': 356, 'Barnsley FC': 357, 'Millwall FC': 384, 'Rotherham United FC': 385,
                    'Bristol City FC': 387, 'Huddersfield Town AFC': 394, 'Brighton & Hove Albion FC': 397,
                     'Brentford FC': 402, 'West Ham United FC': 563, 'England': 770, 'AFC Bournemouth': 1044, 
                     'Burton Albion FC': 1072, 'Preston North End FC': 1081}

    
    return render(request, 'playerInfo/playerInfo.html')
