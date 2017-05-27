import vk
import time
import getpass

APP_ID = 5961701


def get_user_login():
    login = input('Please enter login: ')
    return login


def get_user_password():
    password = getpass.getpass('Please enter password: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    online_friends_ids = api.friends.getOnline()
    friends_online = api.users.get(user_ids=online_friends_ids,
                                   fields=['last_name', 'first_name'])
    return friends_online


def output_friends_to_console(friends_online):
    print('\nYour friends online:')
    for friend_number, friend in enumerate(friends_online, 1):
        print('{}. {} {}'.format(friend_number,
                                 friend.get('first_name'),
                                 friend.get('last_name')))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError as error:
        print(error)
    else:
        output_friends_to_console(friends_online)
