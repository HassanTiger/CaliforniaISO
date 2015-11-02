#  This code is written for python 3.4.3
#  Copyright 2015 James Benson

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Execution: python Oasis.py
#
# WEBSITE: http://oasis.caiso.com/
# DESCRIPTION: 
#   This script downloads data from the California ISO (Independent System 
# Operator) Open Access Same-time Information System. You need to input the 
# groupid you are interested in along with the start & end dates. 
#
# Note: You may need to change the version. Once, executed, a new tab should
#  appear in your webbrowser, begin downloading after a few seconds, and then
#  close automatically.  A new download starts after 30 seconds to prevent
#  flooding the provider.


import datetime
import webbrowser
import time
 
start_date = datetime.date( year = 2013, month = 1, day = 1 )
end_date = datetime.date( year = 2014, month = 1, day = 1 )
groupid = "DAM_LMP_GRP"
version = "1"

list = []
 
if start_date <= end_date:
    for n in range( ( end_date - start_date ).days + 1 ):
        list.append( start_date + datetime.timedelta( n ) )
else:
    for n in range( ( start_date - end_date ).days + 1 ):
        list.append( start_date - datetime.timedelta( n ) )


for d in list:
    url = ('http://oasis.caiso.com/oasisapi/GroupZip?groupid='+groupid+'&startdatetime='+str(d.strftime("%Y%m%d"))+'T00:00-0000&version='+version)
    webbrowser.open_new(url)

# Pause 30 seconds so you dont flood server.
# Minimum of 5 seconds is required between requests.
# Use 30 to account for latency, increased traffic, etc.
    time.sleep(30) 


# Code should download data files as if using web
# http://oasis.caiso.com/oasisapi/GroupZip?groupid=DAM_LMP_GRP&startdatetime=20130919T07:00-0000&version=1