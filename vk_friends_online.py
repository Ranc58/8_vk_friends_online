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
    online_friends_list = []
    for user in online_friends_ids:
        first_name = api.users.get(user_ids=user)[0]['first_name']
        last_name = api.users.get(user_ids=user)[0]['last_name']
        online_friends_list.append(first_name + ' ' + last_name)
        time.sleep(0.7)
    return online_friends_list


def output_friends_to_console(friends_online):
    print('Your friends online:')
    for friend_number, friend in enumerate(friends_online, 1):
        print('{}. {}'.format(friend_number, friend))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    print('\nPlease wait. Getting information.')
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError as error:
        print(error)
    else:
        output_friends_to_console(friends_online)
