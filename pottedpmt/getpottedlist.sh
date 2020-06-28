#########################################################################
# File Name: getpottedlist.sh
# Author: zhaor
# mail: arlier@hit.edu.cn
# Created Time: 2020年06月22日 星期一 12时55分21秒
#########################################################################
#!/bin/bash
#unique list
cat pmtdb.txt|grep Pot | awk '{ print $2  }'|sort|uniq>pottedsnlist.txt
