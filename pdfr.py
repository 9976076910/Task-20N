
import requests


url = "https://labour.gov.in/sites/default/files/ar_2022_23_english.pdf"


response = requests.get(url)


"""
HTTP Response Status Code


1. (100-199) - Informational Responses
2. (200 - 299) - Successful Response
3. (300 - 399) - Redirection messages
4. (400 - 499) - Client Error Response
5. (500 - 599) - Server Error Response


Learn more about this - https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
"""


if response.status_code == 200:
    f = open("Annual Report.pdf", "wb")
    f.write(response.content)
    f.close()
else:
    print("Error")


