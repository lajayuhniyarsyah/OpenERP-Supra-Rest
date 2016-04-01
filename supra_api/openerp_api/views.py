from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from statsd.defaults.django import statsd
from openerp_api import db_setting
import openerplib
import base64




@api_view(['GET','POST'])
def GetModel(request,model,mode=None,fields=[]):
	hostname = db_setting.configrest().host()
	dbname = db_setting.configrest().database_name()
	login = request.data["usn"]
	usrpwd = request.data["pw"]
	fields = request.data["fields"]
	# login_d = 'ricky'
	# usrpwd_d = 'ricky'
	login_d = base64.b64decode(login)
	usrpwd_d = base64.b64decode(usrpwd)
	connection = openerplib.get_connection(hostname=hostname, database=dbname,login=login_d, password=usrpwd_d)
	model_erp = connection.get_model(model)
	if mode==None:
		ids = model_erp.search([],0,100)
	elif mode=="ids":
		ids =map(int, request.data["ids"])
	elif mode=="search":
		searchfield = request.data['searchfield']
		searchoperator = request.data['searchoperator']
		searchcateg = request.data['searchcateg']
		if searchcateg.isdigit():
			searchcateg = int(request.data['searchcateg'])
		print searchfield,searchoperator,searchcateg
		ids = model_erp.search([(searchfield,searchoperator,searchcateg)])
	elif mode == "getupdate":
		last_id=  request.data['ids']
		ids = model_erp.search([('id','>',last_id)],0,100)
	else:
		print "Oops!  That was no valid number.  Try again..."
	if fields ==[]:
		read_model = model_erp.read(ids)
	else:
		read_model = model_erp.read(ids,fields)
	return Response ({"sukses":True,"Result":read_model})

@api_view(['GET','POST'])
def GetJson(request,metode):
	hostname = db_setting.configrest().host()
	dbname = db_setting.configrest().database_name()
	# login = request.data["usn"]
	# usrpwd = request.data["pw"]
	# login_d = base64.b64decode(login)
	# usrpwd_d = base64.b64decode(usrpwd)
	login_d = 'ricky'
	usrpwd_d = 'ricky'
	connection = openerplib.get_connection(hostname=hostname, database=dbname,login=login_d, password=usrpwd_d)
	model_res_user = connection.get_model('res.users')
	model_res_partner = connection.get_model('res.partner')
	
	
	data=[]
	print metode,"ini metode nya "
	if metode =="AllData":
		jsonrpc = openerplib.json_rpc('http://10.36.15.51:8069/sales_activity_plan/Getall','Getall',{'db':db_setting.configrest().database_name()})
		for datajson in jsonrpc:
			read_model_user = model_res_user.read(datajson[4],['name'])
			read_res_partner=''
			if datajson[10]:
				read_res_partner = model_res_partner.read(datajson[10],['name'])
				read_res_partner = read_res_partner['name']
			if datajson[16]==1:
				daylight="Before Lunch / Break"
			elif datajson[16]==2:
				daylight="After Lunch / Break"
			else:
				daylight=""
			data.append({
				'daylight':daylight,
				'name':datajson[9],
				'the_date':datajson[7],
				'location':datajson[11],
				'user':read_model_user['name'],
				'partner':read_res_partner,
				'id':datajson[18],
				'activity_id':datajson[0],
				'user_id':datajson[4],
				'dow':datajson[17],
				'daylight_num':datajson[16]
				})
	elif metode=="GetUpdate":
		# print request.data["idview"],">>>>>>>>>>>>>>"
		jsonrpc = openerplib.json_rpc(
			'http://10.36.15.51:8069/sales_activity_plan/GetID',
			'GetID',{'db':db_setting.configrest().database_name(),
					'activity_id':request.data["activity_id"],
					'user_id':request.data["user_id"],
					'dow':request.data["dow"],
					'daylight':request.data["day_ligth"],
					'idview':request.data["idview"]
					}
			)
		print jsonrpc
		if jsonrpc!=0:
			print "masiiiiiiiiiuuuuuuuuuuuuuukkkkkkkk"
			for datajson in jsonrpc:
				read_model_user = model_res_user.read(datajson[4],['name'])
				read_res_partner=''
				if datajson[10]:
					read_res_partner = model_res_partner.read(datajson[10],['name'])
					read_res_partner = read_res_partner['name']
				if datajson[16]==1:
					daylight="Before Lunch / Break"
				elif datajson[16]==2:
					daylight="After Lunch / Break"
				else:
					daylight=""
				data.append({
					'daylight':daylight,
					'name':datajson[9],
					'the_date':datajson[7],
					'location':datajson[11],
					'user':read_model_user['name'],
					'partner':read_res_partner,
					'id':datajson[18],
					'activity_id':datajson[0],
					'user_id':datajson[4],
					'dow':datajson[17],
					'daylight_num':datajson[16],

					})
	else:
		print "ERROOOORRRR"

	return Response ({"sukses":True,"data":data})

class CustomGet(APIView):

	# @api_view(['GET'])
	def post(self, request, format=None):

		hostname = db_setting.configrest().host()
		dbname = db_setting.configrest().database_name()
		login = request.data["usn"]
		login_d = base64.b64decode(login)

		usrpwd = request.data["pw"]
		usrpwd_d = base64.b64decode(usrpwd)


		connection = openerplib.get_connection(hostname=hostname, database=dbname,login=login_d, password=usrpwd_d)
	
		user_model = connection.get_model("res.users")
		# sale = connection.get_model("sales.activity")
		ids = user_model.search([("company_id", "=", 1)])
		# # # print ids,"BBBBBBBBBBBBBBBBBBBBB"
		# # # if ids:
		# # user_info = user_model.read([0])
		# test = sale.read([3401,3400])
		# print test,"iniii sale order"
	
# # 	# print user_info,"----------->>>"
# # 	name=user_info[0]["name"]

# # else:
# 	name="gk ada"
# print user_info,"BBBBBBBBBBBBBBBBBBBBBBBBBB"


		return Response({"success": True})


	

# class ServiceModel(APIView):



# 	def get(self,request,format=None,model="model"):

# 		return Response({"success": True,"model":model})




















# if model=="sales.activity":

	# 	model_res = connection.get_model('res.users')
	# 	search_kelompok_id = model_res.search([('login','=',login_d)])
	# 	print search_kelompok_id
	# 	read_kelompok_id = model_res.read(search_kelompok_id)
	# 	id_kelompok=[]
	# 	for kelompok in read_kelompok_id:
	# 		id_kelompok.append(kelompok['kelompok_id'][0])
	# 	model_group_sales_line = connection.get_model('group.sales.line')

	# 	search_group_sales_line = model_group_sales_line.search([('kelompok_id','in',id_kelompok)])
	# 	# print search_group_sales_line,"search_group_sales_line"
	# 	ids = model_group_sales_line.read(search_group_sales_line,['name'])

	# 	id_sales_line=[]
	# 	for id_sales in ids:
	# 		print id_sales
	# 		id_sales_line.append(id_sales['name'][0])
	# 	# print "<<<<<<<SSSSSSSSSSSSSSSSSSSSSSS"

	# 	res_param.append(('user_id','in',id_sales_line))
	# 	if len(param):
	# 		res_param.append(('state','in',['draft']))

	# 	print res_param


	# 	ids = model_erp.search(res_param)
	# 	print ids ,"iniii ids"



# @api_view(['GET','POST'])
# def json(request,model,mode=None,fields=[]):

