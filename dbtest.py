import pymysql
def pmttest(contid,massid,drawerid):
		if contid==1:
			conttag="'A'"
		if contid==2:
			conttag="'B'"
		channeltag=str(drawerid+contid*100)
		masstag=str(massid)
		connection=pymysql.connect(db='junopmttest', user='pmtRo', password='JUNO@PanAsia2017', host='202.38.129.227', charset='utf8')
		cursor=connection.cursor()
		exestr="select HV,PMT_ID,BN,Date,Gain_at_setpoints3000,Mu_at_setpoints3000,PDE_at_setpoints3000,PDE_at_setpoints3000_V1,Testing_purpose,HiQE_MCP from junopmttest.container_test where Container_ID= "+conttag +" and  Channel= '"+channeltag +"' and  Mass_ID = '"+masstag+"' order by Date desc limit 0,5"
		cursor.execute(exestr)
		result=cursor.fetchone()
#		if result== None:
#			result="No_Record"
		connection.close()
		#result=result[0]
		return result
