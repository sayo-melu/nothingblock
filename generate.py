# combine all filter-item into filter.txt.

import os
import re
import time

time_version = time.strftime("%Y.%m.%d.%H%M", time.localtime())

head = """\
[Adblock Plus 3.0]
! Title: nothingblock filter
! Description: block unnecessary web element to have 'nothing more to take away'.
! Homepage: https://github.com/dorjmi/nothingblock
! Version: {version}
! Expires: 7 days""".format(version=time_version)

# read item
filter_list = ''
item_dir = 'filter-item/'
item_list = sorted(os.listdir(item_dir))

for i in item_list:
    file = open(item_dir + i, 'r')
    filter_list = filter_list + file.read()
    file.close()

# remove extra
filter_list = re.sub(' *', '', filter_list)
filter_list = re.sub('!.*', '', filter_list)
filter_list = re.sub('[\s]+', '\n', filter_list)

# write to filter.txt
filter = open("filter.txt", "w")
filter.write(head + filter_list)
filter.close()
