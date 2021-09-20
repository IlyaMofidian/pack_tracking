
from crawler import Crawler


def main():

	#for 10 time crawling
	gen_orders = (i for i in range(10)) 

	try:
		while gen_orders:
			order = next(gen_orders)
			c = Crawler(order, threshold= 400)
			# c.test()
			if c.geoChanged():
				c.geoChanged()


	except:
		pass


	# while gen_orders:
	# 	order = next(gen_orders)
	# 	c = Crawler(order, threshold= 200)
	# 	# c.test()
	# 	if c.geoChanged():
	# 		c.geoChanged()



if __name__ == "__main__":
	main() 
