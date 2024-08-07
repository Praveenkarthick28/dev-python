import requests

url = f'https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls'

datas = requests.get(url)

if datas.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = datas.json()

    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}

    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
