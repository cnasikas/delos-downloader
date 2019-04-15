#!/usr/bin/env python3

from multiprocessing.dummy import Pool
from tqdm import tqdm
import requests
import math
import argparse
from bs4 import BeautifulSoup

FILE_BASE_URL = "https://delos-media.uoa.gr:443/delosrc/resources/vl/"
WEB_BASE_URL = "https://delos.uoa.gr/opendelos/player?rid="


def getFileURL(id):
    return FILE_BASE_URL + id + "/" + id + ".mp4"


def getWebSiteURL(id):
    return WEB_BASE_URL + id


def downloadFile(res):
    response = requests.get(res[0])
    soup = BeautifulSoup(response.text, features="html.parser")

    metas = soup.find_all('meta')
    desc = [meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ]
    file = 'downloads/' + desc[0] + '.mp4'

    # Streaming, so we can iterate over the response.
    r = requests.get(res[1], stream=True)

    # Total size in bytes.
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024
    wrote = 0

    with open(file, 'wb') as f:
        for data in tqdm(r.iter_content(block_size), total=math.ceil(total_size // block_size), unit='KB', unit_scale=True):
            wrote = wrote + len(data)
            f.write(data)

    if total_size != 0 and wrote != total_size:
        print("ERROR, something went wrong")


def main():
    parser = argparse.ArgumentParser(description='Delos resource downloader')
    parser.add_argument(
        '-r',
        '--resource',
        nargs='+',
        required=True,
        help='List of space seperated resource ids'
    )
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    args = parser.parse_args()

    resources = [(getWebSiteURL(r), getFileURL(r)) for r in args.resource]

    Pool(4).map(downloadFile, resources)


if __name__ == '__main__':
    main()
