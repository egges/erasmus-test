# get the file using curl
curl "$fileUrl" -o answer.xlsx

# run the checker script
python3 check.py