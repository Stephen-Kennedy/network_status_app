import requests
import requests.exceptions
from logger import update_log_file
from network_status import network_check, ping_check
from send_mail import send_email

default_mail = "medicup@gmail.com"
url = "http://google.com"
ip_address = "8.8.8.8"


def main():
    # check network status
    ping_check(url, ip_address)
# report findings (email)
# send_email(default_mail)
#     print(network_status.status_code)
# except requests.exceptions.ConnectionError:
#     print('There appears to be a problem with the network.')


if __name__ == "__main__":
    main()
