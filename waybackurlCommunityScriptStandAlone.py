
"""

Standalone scripts have no template.
They are only evaluated when you run them. 

"""
#https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server#filtering

import urllib
params = "example.com" #enter your domain here
f = urllib.urlopen("http://web.archive.org/cdx/search/cdx?url="+params+"/*&output=txt&matchType=domain&limit=1000")
print f.read()
