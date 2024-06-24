#!/bin/sh

cd "$(dirname "$0")"


date

echo "------ Get various statistics and put them into one file"
./cpu-script.py

echo "------ convert to png"
# Imagemagick has broken, rsvg-convert is what it calls.
# convert -depth 8 -flatten ./weather-script-output.svg ./weather-script-output.png
rsvg-convert ./cpu-script-output.svg -b white -o ./cpu-script-output.png

echo "------ shrink png"
pngcrush -q -c 2 cpu-script-output.png cpu-script-output_s.png

echo "------ copy to webserver"
cp -f cpu-script-output_s.png /var/www/localhost/htdocs/weather/cpu-script-output.png
