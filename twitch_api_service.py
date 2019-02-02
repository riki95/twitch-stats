import requests
import json

def usersget(headers, users):
        print('Getting user IDs...')
        users_list = []
        for user in users:
                params = {
                ('login', user)
                }
                response = requests.get('https://api.twitch.tv/helix/users', headers=headers, params=params)
                json_string = response.text  # Get the text form response
                json_data = json.loads(json_string)  # Load the JSon file
                users_list.append(json_data["data"][0]['id'])  # Get the ID
        return users_list

def followersget(headers, userIDs):
        print('Getting user followers...')
        users_followers = []
        for userID in userIDs:
                params = (
                ('to_id', userID),
                )
                response = requests.get('https://api.twitch.tv/helix/users/follows', headers=headers, params=params)
                json_string = response.text  # Get the text form response
                json_data = json.loads(json_string)  # Load the JSon file
                users_followers.append(json_data["total"])  # Get the Followers
        return users_followers