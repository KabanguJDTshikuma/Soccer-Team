from django.shortcuts import render
import http.client
import json
from .models import Team


def index(request):
    connection = http.client.HTTPConnection('')
    headers = { 'X-Auth-Token': '' }
    connection.request('GET', '/v2/teams', None, headers )
    url = json.loads(connection.getresponse().read().decode())
    
    teams_dict = {}
    for team in url['teams']:
        teams_dict[team['name']] = team['id']
        
    print(teams_dict)
    team_name = 'Arsenal'

    if 'team_name' in request.GET:
        team_name = request.GET['team_name']

        team_list_dict = {}

        for team in teams_dict.keys():

            if team_name in team:
                connection.request('GET', '/v2/teams/' + str(teams_dict[team]), None, headers )
                url_team = json.loads(connection.getresponse().read().decode())
                team_list_dict['name'] = url_team['name']
                comp = []
                for name in url_team['activeCompetitions']:
                    comp.append(name['name'])
                team_list_dict['competitions'] = ', '.join(comp)
                team_list_dict['color'] = url_team['clubColors']
                team_list_dict['icon'] = url_team['crestUrl']
                team_list_dict['address'] = url_team['address']
                team_list_dict['phone'] = url_team['phone']
                team_list_dict['website'] = url_team['website']
                team_list_dict['stadium'] = url_team['venue']
                team_list_dict['players'] = url_team['squad']
                #print(url_team)
                return render(request, 'player/team.html', {'team_list_dict': team_list_dict})
        else:
            return render(request, 'player/index.html', {'error1': "we dont'have the info this team now. Please try an other one"})
    else:
        return render(request, 'player/index.html', {'error2': "No team much with this name. Please try an other one"})

