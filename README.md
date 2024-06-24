Modified for UK weather - pulled from the Met Office

features:
   - some new icons (we have more types of rain) 
   - changed high/low temp to temp/feels like - this is what the MetOffice give us
   - Wind arrows <-- the best bit!
   

Forked from:
https://github.com/obitoo/kindle-weather-display which was originally forked from http://www.mpetroff.net/archives/2012/09/14/kindle-weather-display/

![Example Screenshot](https://raw.githubusercontent.com/obitoo/kindle-weather-display/master/screenshots/weather-winds.png)

Create a file containing your api key from 

https://www.metoffice.gov.uk/datapoint/api

```
echo "your-api-key" > /script-location/kindle-weather-display/server/apikey
```

Find your location ID from:

http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=<put your api key here>

And update the url line in `./server/new-weather-script.py` (Replace XXXXXXX with your location ID

```
url='http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/XXXXXX?res=daily&key='+myApiKey
```

To use,	the server needs to run	the script, as a cronjob:

```
0 * * * * /script-location/kindle-weather-display/server/weather-script.sh > /dev/null 2>&1
```

You can use Kite (https://www.mobileread.com/forums/showthread.php?t=168270) or (https://www.mobileread.com/forums/showthread.php?t=168270) as launchers, or run the script manually on a kindle via ssh:

Installing them is left as an exercise for the reader, as it varies between versions

Once installed, you can set a cronjob to run the script on the kindle too:

```
[root@kindle root]# mntroot rw
system: I mntroot:def:Making root filesystem writeable
[root@kindle root]# vi /etc/crontab/root 

15 * * * * /mnt/us/weather/display-weather.sh
```

You can also manually run the above command to start the script/update directly.
