source /home/laksshmenarayan/Nyse-converter/nc-venv/bin/activate
export SRC_DIR=/home/laksshmenarayan/Nyse-converter/data/nyse_all/nyse_data
export LOG_FILE_PATH=/home/laksshmenarayan/Nyse-converter/logs/nc.log

rm -rf /home/laksshmenarayan/Nyse-converter/data/nyse_all/nyse_json
nysec
deactivate