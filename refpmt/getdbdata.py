import pymysql
def getall(pmtsn): #list of testid,dim=3xn,[contid,massid,drawerid]
		f = "pmtdb.txt"
		connection=pymysql.connect(db='junopmttest', user='pmtRo', password='JUNO@PanAsia2017', host='202.38.129.227', charset='utf8')
		cursor=connection.cursor()
		exestr="select HV,PMT_ID,BN,Date,Gain_at_0_1pe,Mu_at_0_1pe,PDE_at_0_1pe,Gain_at_setpoints3000,Mu_at_setpoints3000,PDE_at_setpoints3000,PDE_at_setpoints3000_V1,Testing_purpose,HiQE_MCP,Container_ID,Channel, Mass_ID from junopmttest.container_test order by Date desc limit 0,500000"
		cursor.execute(exestr)
		result=cursor.fetchall()
		exestr1="select COLUMN_NAME from  INFORMATION_SCHEMA.Columns where table_name = 'container_test'  and table_schema='junopmttest'"
		cursor.execute(exestr1)
		nameresult=cursor.fetchall()
		print(nameresult)
#		if result== None:
#			result="No_Record"
		connection.close()
		#result=result[0]
		print(len(result))
		with open(f,"w") as file:
			for i in range(0,len(result)):
				if i%3000==0:
					print(result[i])
				#if result[i][1]!=pmtsn:
				#	continue
				for j in range(0,len(result[i])):
					file.write(str(result[i][j])+"\t")
				file.write("\n")
		return 0
getall("EA0574")
