import os
import requests
import datetime


# Create Dumped_Contents folder if it doesn't exist
dumped_contents_path = r'Dumped_Contents'
if not os.path.exists(dumped_contents_path):
    os.mkdir(dumped_contents_path)

# Read HTTP URLs from http_urls.txt file
with open('unique_urls.txt') as file:
    urls = [line.strip() for line in file.readlines()]

# Visit each URL and save its contents to a file in the Dumped_Contents folder
for i, url in enumerate(urls):
    # Make a request to the URL and read its contents
    print(url)
    try:
        response = requests.get(url, timeout=5)  # set timeout to 5 seconds
        contents = response.content
    except requests.exceptions.Timeout:
        # If the request times out, just skip it and move on to the next one
        continue
    except:
        # If there's any other error fetching the URL, just skip it and move on to the next one
        continue
    # Save the contents to a file in the Dumped_Contents folder using a numbered file name
    file_name = f'{i}.html'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'file_{timestamp}.txt'
    print(filename)
    file_name= filename + file_name
    with open(os.path.join(dumped_contents_path, file_name), 'wb') as file:
        file.write(contents)
