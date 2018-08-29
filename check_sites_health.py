import argparse
import whois
import requests


def is_server_respond_with_200(url):
    try:
        return requests.get(url).status_code == 200
    except requests.exceptions.ConnectionError as err:
        return False


def get_domain_expiration_date(url):
    domain = whois.extract_domain(url)
    return whois.whois(domain).expiration_date


def get_path():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", required=True, dest="file_path")
    args = parser.parse_args()
    return args


def read_urls_from_file(path):
    with open(path) as textfile:
        urls = textfile.readlines()
    return list(map(lambda x: x.rstrip(), urls))


def get_url_statuses(urls):
    statuses = []
    for url in urls:
        if is_server_respond_with_200(url):
            status = "Respond"
        else:
            status = "NOT respond"
        expires = get_domain_expiration_date(url) or "<no date>"
        statuses.append([status, expires])
    return zip(urls, statuses)


def print_urls_info(urls_info):
    for url_info in urls_info:
        url, [stat, exp] = url_info
        print("{} - {}, expires {}".format(url, stat, exp))


def main():
    path = get_path().file_path or exit("empty path")
    urls = read_urls_from_file(path)
    url_with_statuses = get_url_statuses(urls)
    print_urls_info(url_with_statuses)


if __name__ == '__main__':
    main()
