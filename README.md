# delos-downloader

A resource downloader for [Delos](https://delos.uoa.gr/opendelos/)

## Installation

1. Install [pipenv](https://pipenv.readthedocs.io/en/latest/)
2. `pipenv install`

## Usage

```
usage: pipenv run python delos-downloader.py [-h] -r RESOURCE [RESOURCE ...] [--version]

Delos resource downloader

optional arguments:
  -h, --help            show this help message and exit
  -r RESOURCE [RESOURCE ...], --resource RESOURCE [RESOURCE ...]
                        List of space seperated resource ids
  --version             show program's version number and exit
```

### Example

`pipenv run python delos-downloader.py -r 3285eba7 34462e14 9b133142`
