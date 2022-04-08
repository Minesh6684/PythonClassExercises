import requests


def search_for_show(show_name):
    res = requests.get('https://api.tvmaze.com/search/shows', params={'q': show_name})

    out = ''
    for result in res.json():
        out += f"{result['show']['id']}: {result['show']['name']} ({result['show']['premiered'][:4]})\n"
    return out


def get_episode_list(show_id):
    res = requests.get(f'https://api.tvmaze.com/shows/{show_id}/episodes')
    out = ''
    for episode in res.json():
        out += f"Season: {episode['season']}\tEpisode: {episode['number']}\t{episode['name']}\n"
    return out


def main():
    print(search_for_show(input('Enter a show name: ')))
    print(get_episode_list(input('Enter Show Id: ')))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
