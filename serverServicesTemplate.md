#!/bin/bash

### Load NVM for root
export NVM_DIR="/root/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

cd /home/system/EUDR-Visualization-System/

pm2 delete all
pm2 start ecosystem.config.js
pm2 startup
pm2 save
echo "restarted nginx server"

/usr/sbin/nginx -s reload


echo "CD repo"
cd /home/system/EUDR-Visualization-System/
echo "====================="
echo "Updating repo..."
echo "====================="
/usr/bin/git pull

cd /home/system/EUDR-Visualization-System/frontend

echo "========================"
echo "Updating dependencies..."
echo "========================"
npm i 
npm run build

### Crontab
@reboot /home/system/update_system.sh >> /var/log/eudr_update_and_build.log 2>&1
@reboot /home/system/start_web_services.sh >> /var/log/eudr_system.log 2>&1
1 * * * * /home/system/update_system.sh >> /var/log/eudr_update_and_build 2>&1