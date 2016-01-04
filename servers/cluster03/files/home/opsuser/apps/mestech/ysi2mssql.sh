#!/bin/bash
##################################################################
#
# Writes data from a kafka to mssql
#
# Script is executed by supervisor,
# see /etc/superviser/conf.d/apps-supervisor.conf
#
################################################################## 
PYTHON=/home/opsuser/virtualenvs/mestech/bin/python
SCRIPT=/home/opsuser/apps/mestech/ysi2mssql.py

. /etc/mestech.conf || ( echo /etc/mestech.conf not found >&2 && exit 1 )

$PYTHON $SCRIPT --db_server="$db_server" --db_user="$db_user" --db_name="$db_name" \
                --db_password="$db_password" --instrument_id "$instrument_id" \
                --site_id="$site_id" --lat="$lat" --lon="$lon"

status=$?
while [ $SECONDS -lt 31 ]; do
    echo -n . >&2
    sleep 1
done
echo "done" $(date) >&2
exit $status