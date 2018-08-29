# Sites Monitoring Utility

Script prints response status of sites and expire date of domain 


## Usage
* You need *.txt file with urls list
* python 3.5 is required to run script
* install requirement modules:
```bash
$ pip install -r requirements.txt
```
* Run:

```bash
$ python check_sites_health.py -p <path_to_textfile>
```
output will be like:
```bash
<url1> - Respond, expires 2019-07-31 21:00:00
<url2> - Respond, expires 2019-07-31 21:00:00
<url3> - NOT respond, expires <no date>
<url4> - Respond, expires 2019-07-31 21:00:00
```

### Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
