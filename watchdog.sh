#! /bin/bash

#pyradmon_watchdog.sh
# Checks to see if pyradmon is running if not, restarts.
# Log entries are appended to existing log file.
# Call from cron job every X minutes.
# *******************************************************
# 2014-01-03 Radslug v1.0 initial version
# 2014-03-11 Modified for Ubuntu 13 installation by Erix1
# *******************************************************

# Create datetime stamp for file name
# (or use: /varlog/$(date -d "today" +"%Y%m%d%H%M").log )
DATE=$(date +"%Y%m%d%H%M")

case "$(pidof myradmon.py | wc -w)" in

0)  echo "Restarting pyradmon.py:     $(date)" >> /opt/radmon/watchdog.log
    /usr/bin/nohup ./myradmon.py &
    ;;
1)  # all ok
    ;;
*)  echo "Removed double pyradmon.py: $(date)" >> /opt/radmon/watchdog.log
    kill $(pidof myradmon.py | awk '{print $1}')
    ;;
esac

# 0 If process is not found, restart it.
# 1 If process is found, all ok.
# * If process running 2 or more, kill the last.
