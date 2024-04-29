from flask import Flask, request, jsonify
from user_agent import generate_user_agent
import requests
from uuid import uuid4

app = Flask(__name__)

@app.route('/instagram_info/<user>', methods=['GET'])
def get_instagram_info(user):
        he = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en;q=0.9',
            'cookie': f'ig_did={uuid4()}; datr=8J8TZD9P4GjWjawQJMcnRdV_; mid=ZBOf_gALAAGhvjQbR29aVENHIE4Z; ig_nrcb=1; csrftoken=5DoPPeHPd4nUej9JiwCdkvwwmbmkDWpy; ds_user_id=56985317140; dpr=1.25',
            'referer': f'https://www.instagram.com/{user}/?hl=ar',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'viewport-width': '1051',
            'x-asbd-id': '198387',
            'x-csrftoken': '5DoPPeHPd4nUej9JiwCdkvwwmbmkDWpy',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }

        rr = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}', headers=he)
        if 'data' in rr.text:
            by = '@te9egram'
            try:
                Id = rr.json()['data']['user']['id']
            except:
                Id = ""
            try:
                name = rr.json()['data']['user']['full_name']
            except:
                name = ""
            try:
                bio = rr.json()['data']['user']['biography']
            except:
                bio = ""
            try:
                flos = rr.json()['data']['user']['edge_followed_by']['count']
            except:
                flos = ""
            try:
                flog = rr.json()['data']['user']['edge_follow']['count']
            except:
                flog = ""
            try:
                pr = rr.json()['data']['user']['is_private']
            except:
                pr = ""

            try:
                re = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()
                da = re['date']
            except:
                da = 'No Date'

            return jsonify({
                'name': name,
                'user': user,
                'followers': flos,
                'following': flog,
                'date': da,
                'id': Id,
                'bio': bio,
                'private': pr,
                'BY': by
            })



if __name__ == '__main__':
    app.run(debug=True)
