import requests
import sys


def brute(url, wordlist):
    for word in wordlist:
        try:
            url_final = f"{url}/{word}"
            response = requests.get("http://g1.com")
            code = response.status_code
            if code != 404:
                print(f"{url_final}  ---  {code}")
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass
        


if __name__ == "__main__":
    args = sys.argv
    url = args[1]
    wordlist = args[2]
    with open(wordlist, "r") as file:
        wordlist = file.readlines()

    brute(url, wordlist)
