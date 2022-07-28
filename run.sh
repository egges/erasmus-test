# print the file url
echo "$fileUrl"

# get the file using curl
curl "$fileUrl" -o answer.xlsx

ls -l

# run the checker script
python3 check.py

echo "Done!"