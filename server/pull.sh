#!/bin/bash

# get keys
cd ~/Desktop/code/Sbus/server
source ./keys.sh

# retrieve data from ftp server
ftp -in <<EOF
open $ftp_site
user $username $passwd
get google_transit.zip
EOF

# unload data
unzip google_transit.zip
