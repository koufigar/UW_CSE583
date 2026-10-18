mkdir pronto
touch READ.txt
echo "this is info about the data" > READ.text
mkdir data
cd data/
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head *.csv

