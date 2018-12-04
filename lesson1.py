S = "De l'audace, encore de l'audace, toujours de l'audace"
index = 0
found_list = []

while True:
    found = S.find('audace', index)
    if found != -1:
        found_list.append(found)
    else:
        break
    index = found + 1

print(found_list)

'''<a href="<url>">'''
PAGE = '<a href="http://udacity.com">Hello world</a><a href="http://udacity.com">Hello world</a><a href="http://third.com">Hello world</a>'
HREF = '<a href='
page_index = 0
url_list = []

while True:
    foundHref = PAGE.find(HREF, page_index)
    print("found href: %s" %foundHref)
    if foundHref != -1:
        found_start = PAGE.find('"', foundHref)
        found_end = PAGE.find('">', found_start + 1)
        #print("Found indices: %s %s" %(found_start, found_end))
        url = PAGE[found_start+1:found_end]
        print("Url: " + url)
        url_list.append(url)
    else:
        break
    page_index = foundHref + 1
print(url_list)
