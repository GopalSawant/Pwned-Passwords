import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f' error fetching {res.status_code},check the API and try  again')
    return res


def get_password_count(response_hash, our_password_tail):
    response_hash = (line.split(':') for line in response_hash.text.splitlines())
    for h, count in response_hash:
        if h == our_password_tail:
            return count
    return 0


def pawned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    # print(first5_char, tail)
    response = request_api_data(first5_char)
    # print(response.text)
    return get_password_count(response, tail)


def main(args):
    for password in args:
        count = pawned_api_check(password)
        if count:
            print(f'{password} was fount {count} times .....and you should probably change the password ')
        else:
            print(f'{password} Carry on')


if __name__ == '__main__':
    ar = sys.argv = ['hello']
    main(ar)
