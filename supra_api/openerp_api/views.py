from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from statsd.defaults.django import statsd
import openerplib
import base64




@api_view(['GET','POST'])
def GetModel(request,model,mode=None,fields=[]):
	# print request.path,"=",'/openerp/'+model+'/ids/'
	

	hostname = "localhost"
	dbname = "belajarerp"
	login = request.data["usn"]
	usrpwd = request.data["pw"]
	fields = request.data["fields"]


	# param = [3401] #list id model


	# login_d = 'ricky'
	# usrpwd_d = 'ricky'

	login_d = base64.b64decode(login)
	usrpwd_d = base64.b64decode(usrpwd)
	
	

	connection = openerplib.get_connection(hostname=hostname, database=dbname,login=login_d, password=usrpwd_d)
	model_erp = connection.get_model(model)
	
	
	if mode==None:
		ids = model_erp.search([],0,100)
		# ids = model_erp.search([('id','>',1235678)])
	elif mode=="ids":
		# print request.data["ids"],"<<<<<<<<<<<<<<<<<<<<<<"
		ids =map(int, request.data["ids"])
		# ids = [3401]
	elif mode=='jsonrpc':
		jsonrpc = openerplib.json_rpc('http://10.36.15.51:8069/sales_activity_plan','index',[])
		return Response ({"sukses":True,"data":jsonrpc})
	elif mode=="search":
		searchfield = request.data['searchfield']
		searchoperator = request.data['searchoperator']
		searchcateg = request.data['searchcateg']
		if searchcateg.isdigit():
			searchcateg = int(request.data['searchcateg'])

		print searchfield,searchoperator,searchcateg
		ids = model_erp.search([(searchfield,searchoperator,searchcateg)])
		# ids = request.data['nama']
		# print "ini yang search bro"
	elif mode == "getupdate":
		last_id=  request.data['ids']
		# print last_id,"bebas"
		ids = model_erp.search([('id','>',last_id)],0,100)
		# print ids ,"cek"
	else:
		print "Oops!  That was no valid number.  Try again..."

	# if model_erp.search(param):
	
	# if request.path =='/openerp/'+model+'/ids/':
	# 	ids =int(request.query_params['ids'])
	# elif request.path =='/openerp/'+model+'/search/':
	# 	print "yang elif"
	# else:
	# 	ids = model_erp.search([])
	# print ids,"<<<<<<<<"
	if fields ==[]:
		read_model = model_erp.read(ids)
	else:
		read_model = model_erp.read(ids,fields)
	return Response ({"sukses":True,"Result":read_model})
# @api_view(['GET','POST'])
# def GetJson(request):
# 	connection = openerplib.get_connection(hostname=hostname, database=dbname,login=login_d, password=usrpwd_d)
# 	jsonrpc = openerplib.json_rpc('http://10.36.15.51:8069/coba/test','test',[])
# 	return Response ({"sukses":True,"data":jsonrpc})

# 3371
# 3298
class CustomGet(APIView):

	# @api_view(['GET'])
	def post(self, request, format=None):

		hostname = "localhost"
		dbname = "belajarerp"
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


	

class ServiceModel(APIView):



	def get(self,request,format=None,model="model"):

		return Response({"success": True,"model":model})




















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

