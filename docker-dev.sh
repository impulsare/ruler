#!/bin/bash
useradd -m -u 1000 app > /dev/null 2>&1

COMPONENTS=( extractor config distributer job logger ruler writer )
for COMPONENT in "${COMPONENTS[@]}"; do
    su - app -c "python -c 'import impulsare_${COMPONENT}'" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "${COMPONENT} already installed"
    else
        echo "Installing ${COMPONENT}"
        su - app -c "pip install --upgrade --user -e /components/${COMPONENT}" > /dev/null
        su - app -c "pip install --upgrade --user -r /components/${COMPONENT}/requirements-dev.txt" > /dev/null
    fi
done

echo "Done installing components !"

echo "Starting listener"
while sleep 2; do
    running=$(ps -ef | grep "queue-listener" | wc -l | tr -d ' ')
    if [ $running -gt 1 ]; then
        exit 0
    fi
    echo "."
    su - app -c "CONFIG_FILE=/home/app/conf/config.yml /home/app/.local/bin/queue-listener -h redis -q ruler"
done
