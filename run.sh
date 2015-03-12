#!/bin/bash

apikey=$1
echo "Using API-key: $apikey"

get_data() {
    from_date=$1
    to_date=$2
    data="${apikey}\n${from_date}\n${to_date}\n"
    echo -e $data | ./rescuetime_exporter/main.py
    echo -e "\n\n"
}

get_data "2013-09-01" "2014-01-01"
get_data "2014-01-01" "2014-03-01"
get_data "2014-03-01" "2014-06-01"
get_data "2014-06-01" "2014-09-01"
get_data "2014-09-01" "2014-11-01"
get_data "2014-11-01" "2015-01-01"
get_data "2015-01-01" "2015-03-01"
