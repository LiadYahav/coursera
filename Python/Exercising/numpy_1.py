import requests
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path="C:\\Users\Liad\Downloads\example1.txt"
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
    