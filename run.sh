# get the file using curl
curl "$fileUrl" -o answer.xlsx -s

# run the checker script
python3 check.py