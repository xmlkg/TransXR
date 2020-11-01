from xml.dom.minidom import parse

def readXML():
	filename = './auction_preprocess.xml'
	domTree = parse("./standard.xml")
	#文档根元素site
	rootNode = domTree.documentElement
	#site子元素regions
	region = rootNode.getElementsByTagName("regions")[0]
	regions_var = ["africa","asia","australia","europe","namerica","samerica"]
	item_iterate = 0
	for i in range(len(regions_var)):
		area = region.getElementsByTagName(regions_var[i])[0]
		# with open(filename,'a') as file_object:
		# 	file_object.write(str(region.nodeName) + str(" null") + str(" null") + ' ' + str(area.nodeName) + str(" null") + str(" null") + str('\n'))
		#area子元素item
		items = area.getElementsByTagName("item")
		for item in items:
			if item.hasAttribute("id"):
				# location元素
				location = item.getElementsByTagName("location")[0]
				# quantity元素
				quantity = item.getElementsByTagName("quantity")[0]
				# name元素
				name = item.getElementsByTagName("name")[0]
				# payment元素
				payment = item.getElementsByTagName("payment")[0]
				# shipping元素
				shipping = item.getElementsByTagName("shipping")[0]
				# incategory元素列表
				incategories = item.getElementsByTagName("incategory")
				# item_name = str(item.nodeName) + str(item_iterate)
				incategory_var = ""
				for incategory in incategories:
					if incategory.hasAttribute("category"):
						incategory_nodename = str(incategory.nodeName)
						incategory_getattribute = str(incategory.getAttribute("category"))
						incategory_var = incategory_var +' '+ incategory_nodename + ' ' +"category"+' '+ incategory_getattribute + " null" + " null "
				# # mailbox元素
				# mailbox = item.getElementsByTagName("mailbox")[0]
				# # mail元素
				# mail = mailbox.getElementsByTagName("mail")
				# if(len(mail) > 0):
				# 	mail_var = ''
				# 	for i in range(len(mail)):
				# 		date = mail[i].getElementsByTagName("date")[0]
				# 		mail_var = mail_var + ' ' + str(mail[i].nodeName) + str(i) + ' '+ str(mail[i].nodeName) + str(" null") + str(" null") + ' ' + str(date.nodeName) + ' ' + str(date.childNodes[0].data.replace(' ','_')) + str(" null") + str(" null")
				# else:
				# 	mail_var = ''
				with open(filename,'a') as file_object:
					if len(payment.childNodes) > 0:
						payment_var = payment.childNodes[0].data.replace(' ','_')
					else:
						payment_var = ''
					if len(shipping.childNodes) > 0:
						shipping_var = shipping.childNodes[0].data.replace(' ','_')
					else:
						shipping_var = ''
					#   + ' ' +
					file_object.write(str(item.nodeName)+' '+str("id") + ' ' + str(item.getAttribute("id")) + str(" null") + str(" null") + ' ' +
					 str(location.nodeName) + ' ' + str(location.childNodes[0].data.replace(' ','_')) + str(" null") + str(" null") + ' ' + 
					str(quantity.nodeName) + ' ' + str(quantity.childNodes[0].data.replace(' ','_')) + str(" null") + str(" null") + ' ' +
					str(name.nodeName) + ' ' + str(name.childNodes[0].data.replace(' ','_')) + str(" null") + str(" null") + ' ' + 
					str(payment.nodeName) + ' ' + str(payment_var) + str(" null") + str(" null") + ' ' + 
					str(shipping.nodeName) + ' ' + str(shipping_var) + str(" null") + str(" null") + ' ' + str(incategory_var) + str('\n'))	
				#item_iterate = item_iterate + 1
	
	# categories元素
	categor_ies = rootNode.getElementsByTagName("categories")[0]
	# 所有的 category 元素
	categories = categor_ies.getElementsByTagName("category")
	# category_iterate = 0
	for category in categories:
		if category.hasAttribute("id"):
			# name 元素
			name = category.getElementsByTagName("name")[0]
			#cat_name = str(category.nodeName)+str(category_iterate)
			with open(filename,'a') as file_object:
				file_object.write(str(category.nodeName)+' '+"id "+str(category.getAttribute("id"))+str(" null") + str(" null") + ' '+
					str(name.nodeName)+' '+str(name.childNodes[0].data.replace(' ','_'))+str(" null") + str(" null") + str("\n"))
		# category_iterate = category_iterate + 1
	
	# catgraph元素
	catgraph = rootNode.getElementsByTagName("catgraph")[0]
	#所有的 edge元素
	edges = catgraph.getElementsByTagName("edge")
	for edge in edges:
		with open(filename,'a') as file_object:
			file_object.write(str(edge.nodeName)+' '+"from"+' '+str(edge.getAttribute("from"))+str(" null") + str(" null")+' '+"to "+str(edge.getAttribute("to")+str(" null") + str(" null")+str("\n")))

	# people元素
	people = rootNode.getElementsByTagName("people")[0]
	# 所有的person元素
	persons = people.getElementsByTagName("person")
	median_null = " null"+" null"
	for person in persons:
		if person.hasAttribute("id"):
			# name元素
			name = person.getElementsByTagName("name")[0]
			# emailaddress元素
			emailaddress=person.getElementsByTagName("emailaddress")[0]
			# phone 元素
			phone = person.getElementsByTagName("phone")
			if len(phone)==1:
				phone_var = str(phone[0].nodeName)+' '+str(phone[0].childNodes[0].data.replace(' ','_'))+median_null+' '
			else:
				phone_var = ""
			# homepage元素
			homepage = person.getElementsByTagName("homepage")
			if len(homepage)==1:
				homepage_var = str(homepage[0].nodeName)+' '+str(homepage[0].childNodes[0].data.replace(' ','_'))+median_null+' '
			else:
				homepage_var = ""
			# creditcard元素
			creditcard = person.getElementsByTagName("creditcard")
			if len(creditcard)==1:
				creditcard_var = str(creditcard[0].nodeName)+' '+str(creditcard[0].childNodes[0].data.replace(' ','_'))+median_null+' '
			else:
				creditcard_var = ""
			# address元素
			address = person.getElementsByTagName("address")
			if len(address)>0:
				# street元素
				street = address[0].getElementsByTagName("street")[0]
				# city元素
				city = address[0].getElementsByTagName("city")[0]
				# province元素
				province = address[0].getElementsByTagName("province")
				if len(province)==1:
					province_var = str(province[0].nodeName)+' '+str(province[0].childNodes[0].data.replace(' ','_'))+median_null+' '
				else:
					province_var = ""
				# zipcode元素
				zipcode = address[0].getElementsByTagName("zipcode")[0]
				# country元素
				country = address[0].getElementsByTagName("country")[0]
				address_var = str(address[0].nodeName)+' '+str(street.nodeName) + " " + str(street.childNodes[0].data.replace(' ','_')) + median_null + " " + str(city.nodeName)+' '+str(city.childNodes[0].data.replace(' ','_'))+median_null+' '+str(province_var)+str(zipcode.nodeName)+' '+str(zipcode.childNodes[0].data.replace(' ','_'))+median_null+' '+str(country.nodeName)+' '+str(country.childNodes[0].data.replace(' ','_'))+median_null
			else:
				address_var = ''
			#profile元素
			profile = person.getElementsByTagName("profile")
			if len(profile)>0:
				#interest元素
				interests = profile[0].getElementsByTagName("interest")
				interest_var = ""
				for interest in interests:
					interest_var = interest_var+' '+str(interest.nodeName)+' '+str("category")+' '+str(interest.getAttribute("category"))+median_null 
				#education元素
				education = profile[0].getElementsByTagName("education")
				if len(education)>0:
					eduction_var = str(education[0].nodeName)+' '+str(education[0].childNodes[0].data.replace(' ','_'))
				else:
					eduction_var = ""
				#business元素
				business = profile[0].getElementsByTagName("business")[0]
				#age元素
				age = profile[0].getElementsByTagName("age")
				if len(age)>0:
					age_var = str(age[0].nodeName)+' '+str(age[0].childNodes[0].data.replace(' ','_'))
				else:
					age_var = ""
				profile_var = str(profile[0].nodeName)+" income "+str(profile[0].getAttribute("income"))+median_null+' '+interest_var+' '+\
				eduction_var+median_null+' '+str(business.nodeName)+' '+str(business.childNodes[0].data.replace(' ','_'))+median_null+' '+\
				age_var+median_null
			watch_var = ""
			watches = person.getElementsByTagName("watches")
			if len(watches)>0:
				watch = watches[0].getElementsByTagName("watch")
				if len(watch)>0:
					watch_var = " watches"
					for w in watch:
						watch_var = watch_var+' '+str(w.nodeName)+' '+"open_auction"+' '+str(w.getAttribute("open_auction"))+median_null
			with open(filename,'a') as file_object:
				file_object.write(str(person.nodeName)+str(" id")+' '+str(person.getAttribute("id"))+median_null+
					' '+str(name.nodeName)+' '+str(name.childNodes[0].data.replace(' ','_'))+median_null+' '+
					str(emailaddress.nodeName)+' '+str(emailaddress.childNodes[0].data.replace(' ','_'))+median_null+' '+phone_var+homepage_var+address_var+
					creditcard_var+profile_var+watch_var+str("\n")
					)

	# open_acutions元素
	open_auctions = rootNode.getElementsByTagName("open_auctions")[0]
	# 所有的 open_auction 元素
	all_open_auction = open_auctions.getElementsByTagName("open_auction")
	for openauction in all_open_auction:
		if openauction.hasAttribute("id"):
			#openauc = str(openauction.nodeName)+str(openauction_iterate)
			#initial元素
			initial = openauction.getElementsByTagName("initial")[0]
			#reserve元素
			# reserve = openauction.getElementsByTagName("reserve")
			# if len(reserve)>0:
			# 	reserve_var = str(reserve[0].nodeName)+' '+str(reserve[0].childNodes[0].data.replace(' ','_'))+median_null
			# else:
			# 	reserve_var = ""
			#bidder元素
			bidder = openauction.getElementsByTagName("bidder")
			if len(bidder)>0:
				#date元素
				date = bidder[0].getElementsByTagName("date")[0]
				#time元素
				time = bidder[0].getElementsByTagName("time")[0]
				#personref元素
				personref = bidder[0].getElementsByTagName("personref")[0]
				#increase元素
				increase = bidder[0].getElementsByTagName("increase")[0]
				bidder_var = str(bidder[0].nodeName)+' '+str(date.nodeName)+' '+str(date.childNodes[0].data.replace(' ','_'))+median_null+' '+\
					str(time.nodeName)+' '+str(time.childNodes[0].data.replace(' ','_'))+median_null+' '+str(personref.nodeName)+' '+str("person")+' '+\
					str(personref.getAttribute("person"))+median_null+' '+str(increase.nodeName)+' '+str(increase.childNodes[0].data.replace(' ','_'))
			else:
				bidder_var = ""
			#current元素
			current = openauction.getElementsByTagName("current")[0]
			#itemref元素
			itemref = openauction.getElementsByTagName("itemref")[0]
			#seller元素
			seller = openauction.getElementsByTagName("seller")[0]
			#quantity元素
			quantity = openauction.getElementsByTagName("quantity")[0]
			#type元素
			type_1 = openauction.getElementsByTagName("type")[0]
			#interval元素
			interval = openauction.getElementsByTagName("interval")[0]
			#start元素
			start = interval.getElementsByTagName("start")[0]
			#end元素
			end = interval.getElementsByTagName("end")[0]
			#annotation元素
			annotation = openauction.getElementsByTagName("annotation")[0]
			#author元素
			author = annotation.getElementsByTagName("author")[0]
			#happiness元素
			happiness = annotation.getElementsByTagName("happiness")[0]
			with open(filename,'a') as file_object:
				file_object.write(str(openauction.nodeName)+" id "+str(openauction.getAttribute("id"))+median_null+' '+
					str(initial.nodeName)+' '+str(initial.childNodes[0].data.replace(' ','_'))+median_null+' '+
					#reserve_var+' '+
					bidder_var+median_null+' '+
					str(current.nodeName)+' '+str(current.childNodes[0].data.replace(' ','_'))+median_null+' '+
					str(itemref.nodeName)+' '+"item"+' '+str(itemref.getAttribute("item"))+median_null+' '+
					str(seller.nodeName)+' '+"person"+' '+str(seller.getAttribute("person"))+median_null+' '+
					str(quantity.nodeName)+' '+str(quantity.childNodes[0].data.replace(' ','_'))+median_null+' '+
					str(type_1.nodeName)+' '+str(type_1.childNodes[0].data.replace(' ','_'))+median_null+' '+"interval"+' '+
					str(start.nodeName)+' '+str(start.childNodes[0].data.replace(' ','_'))+median_null+' '+
					str(end.nodeName)+' '+str(end.childNodes[0].data.replace(' ','_'))+median_null+' '+
					"annotation"+' '+str(author.nodeName)+' '+"person"+' '+str(author.getAttribute("perso"))+' '+
					"happiness"+' '+str(happiness.childNodes[0].data.replace(' ','_'))+median_null+str("\n"))

	#closed_auctions元素
	closed_auctions = rootNode.getElementsByTagName("closed_auctions")[0]
	#所有closed_auction元素
	all_closed_auctions = closed_auctions.getElementsByTagName("closed_auction")
	#closedauction_iterate = 0
	for closedauction in all_closed_auctions:
		#closedauc = str(closedauction.nodeName)+str(closedauction_iterate)
		#seller元素
		seller = closedauction.getElementsByTagName("seller")[0]
		#buyer元素
		buyer = closedauction.getElementsByTagName("buyer")[0]
		#itemref元素
		itemref = closedauction.getElementsByTagName("itemref")[0]
		#price元素
		price = closedauction.getElementsByTagName("price")[0]
		#date元素
		date = closedauction.getElementsByTagName("date")[0]
		#quantity元素
		quantity = closedauction.getElementsByTagName("quantity")[0]
		#type元素
		type_2 = closedauction.getElementsByTagName("type")[0]
		#annotation元素
		annotation = closedauction.getElementsByTagName("annotation")[0]
		#author元素
		author = annotation.getElementsByTagName("author")[0]
		#happiness元素
		happiness = annotation.getElementsByTagName("happiness")[0]
		with open(filename,'a') as file_object:
				file_object.write(str(closedauction.nodeName)+' '+
					str(seller.nodeName)+' '+"person "+str(seller.getAttribute("person"))+median_null+' '+
					str(buyer.nodeName)+' '+"person "+str(buyer.getAttribute("person"))+median_null+' '+
					str(itemref.nodeName)+' '+"item "+str(itemref.getAttribute("item"))+median_null+' '+
					str(price.nodeName)+' '+str(price.childNodes[0].data.replace(' ','_'))+median_null+' '+
					str(date.nodeName)+' '+str(date.childNodes[0].data.replace(' ','_'))+median_null+' '+
					str(quantity.nodeName)+' '+str(quantity.childNodes[0].data.replace(' ','_'))+median_null+' '+
					str(type_2.nodeName)+' '+str(type_2.childNodes[0].data.replace(' ','_'))+median_null+' '+
					"annotation"+' '+str(author.nodeName)+' '+"person"+' '+str(author.getAttribute("person"))+' '+
					"happiness"+' '+str(happiness.childNodes[0].data.replace(' ','_'))+median_null+str("\n"))
					
		#closedauction_iterate = closedauction_iterate + 1
if __name__ == '__main__':
	readXML()