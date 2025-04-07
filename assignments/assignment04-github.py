import requests
from config import apykeys as cfg #Access my api keys in config file
from github import Github

# URL of my private github repo
targetrepo = 'gfmg/aprivateone'

#Filename to process
filename = 'test_file.txt'

# Name of the API key of interest to use to access the above url
apikey = cfg['githubMaster']
#Establish connection to the private repo
g=Github(apikey)
# Get the repo object and url of filename indicated above
repo = g.get_repo(targetrepo)
fileInfo = repo.get_contents(filename)
urlfile = fileInfo.download_url

# Response from the file URL
response = requests.get(urlfile)

#Handle response
if(response.status_code == 200):
    print("File downloaded successfully.")
    res = response.text # Get file content if succesful
else:
    print(f"Failed to download file. Status code: {response.status_code}")

# Replace every instance of 'Andrew' with 'Guillermo' in the file content
out = res.replace('Andrew', 'Guillermo')

# Commit the changes back to the repo
gitHubResponse=repo.update_file(fileInfo.path, "Andrew to Guillermo modification", out, fileInfo.sha)
print(gitHubResponse)