
"""
Targeted scripts can only be invoked by you, the user, e.g. via a right-click option on the Sites or History tabs
"""
import urllib
def invokeWith(msg):
  # Debugging can be done using print like this
  print('invokeWith called for url=' + msg.getRequestHeader().getURI().toString()); 
  URL=msg.getRequestHeader().getURI().toString();
  f = urllib.urlopen("http://web.archive.org/cdx/search/cdx?url="+URL+"/*&output=txt&matchType=domain&limit=1000&collapse=urlkey&matchType=prefix&showDupeCount=true")
  print f.read()

