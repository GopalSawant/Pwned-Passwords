import requests
import hashlib


def hash_key_password(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    sha1_head = sha1_password[:5]
    sha1_tail = sha1_password[5:]
    # print(sha1_head, sha1_tail)
    response = api_check(sha1_head)
    return get_password_count(response, sha1_tail)



def api_check(head_string):
    url = "https://api.pwnedpasswords.com/range/" + head_string
    response_from_api = requests.get(url)
    # print(response_from_api.text)
    return response_from_api


def get_password_count(all_response_from_api, password_tail):
    all_hash_key = (line.split(':') for line in all_response_from_api.text.splitlines())

    for tail_hash_key, count in all_hash_key:
        if tail_hash_key==password_tail:
            print(count)
    return 0


hash_key_password('hello')
