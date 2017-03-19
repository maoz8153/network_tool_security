import threading
import urllib2
import time

start = time.time()
urls = ["http://tmla.sandbox.uccentral.att.com:9080/api/case?filters=%7B%22nested%22:%5B%7B%22filter_by%22:%22id%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D,%7B%22filter_by%22:%22created_by%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D,%7B%22filter_by%22:%22editor_name%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D,%7B%22filter_by%22:%22description%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D%5D,%22logic%22:%22and%22%7D&filters=%7B%22filter_by%22:%22_company_id%22,%22filter%22:%22eq%22,%22value%22:%22POC%22,%22logic%22:%22and%22%7D&page=1&page_size=20", "http://tmla.sandbox.uccentral.att.com:9080/api/alert?filters=%7B%22nested%22:%5B%7B%22filter_by%22:%22id%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D,%7B%22filter_by%22:%22source.ip%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D,%7B%22filter_by%22:%22source.port%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D,%7B%22filter_by%22:%22source.hostname%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D,%7B%22filter_by%22:%22target.ip%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D,%7B%22filter_by%22:%22target.port%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D,%7B%22filter_by%22:%22target.hostname%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D,%7B%22filter_by%22:%22alert.title%22,%22filter%22:%22match%22,%22value%22:%22test%22,%22logic%22:%22or%22%7D%5D,%22logic%22:%22and%22%7D&filters=%7B%22filter_by%22:%22_company_id%22,%22filter%22:%22eq%22,%22value%22:%22POC%22,%22logic%22:%22and%22%7D&page=1&page_size=20"]

def fetch_url(url):
    urlHandler = urllib2.urlopen(url)
    html = urlHandler.read()
    print "'%s\' fetched in %ss" % (url, (time.time() - start))


for i in range(100):
    for url in urls:
        fetch_url(url)
        

print "Elapsed Time: %s" % (time.time() - start)
