import urllib3

# create an instance of the `urllib3` pool manager
http = urllib3.PoolManager(num_pools=10)

# prompt the user for the URL
url = input('Enter the URL: ')

# prompt the user for the wordlist file path
wordlist_file = input('Enter the path to the wordlist file: ')

# read the wordlist from the file
with open(wordlist_file) as f:
    wordlist = f.readlines()

# iterate through the wordlist and fuzz the URL
for word in wordlist:
    # strip the newline character from the word
    word = word.strip()

    # fuzz the URL with the word
    fuzzed_url = url + word

    # make a request to the fuzzed URL
    response = http.request('GET', fuzzed_url)

    # check the status code of the response
    if response.status == 200:
        # if the response is successful, print the fuzzed URL
        print(f'Success: {fuzzed_url}')
    else:
        # if the response is unsuccessful, print the status code and the fuzzed URL
        print(f'Error {response.status}: {fuzzed_url}')
