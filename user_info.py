import json
import codecs
from pathlib import Path
from app.user_data import user_data


def nuw_user(user_id, username, user_class):
    data_user = {
        'username': username,
        'user_class': user_class
    }

    user_data[user_id] = data_user

"""
    path = Path('app/user_data.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    if user_id not in data:
        print(data)
        print(type(data))
        data[user_id] = data_user
        path.write_text(json.dumps(data, indent=4), encoding='utf-8')
"""

nuw_user('11', 'admin', '10')