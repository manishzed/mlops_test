# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "https://9af6-2405-201-a404-981b-91a7-953f-a797-df7a.in.ngrok.io/train"

# data to be sent to api
data = {
	"url": "https://github.com/manishzed/mlops_mlflow_v1",
	"branch_name": "master",
	"algo_type": "Regression"
}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)
