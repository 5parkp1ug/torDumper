from datetime import datetime
import sqlite3
import os
import csv
import urllib

class readFile:
		
	def __init__(self):
		self.lineCount = 0
		self.data = []
		self.checkDB()
		
		
	def checkDB(self):
		if os.path.isfile('data.db'):
			print "Database Exists...!!!"
			op = raw_input("Do you want to View data or Update?(Default is View)[V/U] ")
			if (op=='U' or op=='u'):
				self.update_DB()
			else:
				print "!!!...Data in DB...!!!"
				self.disp_info()
			#Check if update is required by accessing the file and comparing the md5

		else:
			print "It seems that the DB doesn't exist. Creating One Now!!!"
			self.create_DB()


	def disp_info(self):
		print "I will display info"
		connection = self.connect_db()
		cur = connection.cursor()
		cur.execute("SELECT * FROM TORDATA")
		rows = cur.fetchall()
		print rows

	def update_DB(self):
		print "I will insert info and Update the Database"
		
		#get the file contents
		url = urllib.urlopen('https://torstatus.blutmagie.de/query_export.php/Tor_query_EXPORT.csv')
		dump = url.readlines()
		
		self.connection = self.connect_db()
		cur = connection.cursor()
		connection.execute('''INSERT INTO TORDATA (ROUTER_NAME,COUNTRY,BANDWIDTH,UPTIME,IP_ADDR,HOSTNAME,OR_PORT,DIR_PORT,PLATFORM,FIRST_SEEN,AS_NAME,AS_NUMBER,C_BANDWIDTH,OR_ADDR) 
		VALUES (data["ROUTER_NAME"],data["COUNTRY"],data["BANDWIDTH"],data["UPTIME"],data["IP_ADDR"],data["HOSTNAME"],data["OR_PORT"],data["DIR_PORT"],data["PLATFORM"],data["FIRST_SEEN"],data["AS_NAME"],data["AS_NUMBER"],data["C_BANDWIDTH"],data["OR_ADDR"]);''')
		connection.commit()
		connection.close()
		

	def create_DB(self):
		#create database
		'''
		#fetch the file
		url = urllib.urlopen('https://torstatus.blutmagie.de/query_export.php/Tor_query_EXPORT.csv')
		dump = url.readlines()
		'''
		connection = self.connect_db()
		cur = connection.cursor()
		if cur:
			print cur
			cur.execute('''CREATE TABLE TORDATA
						(ID INTEGER PRIMARY KEY AUTOINCREMENT,
						ROUTER_NAME varchar(25),
						COUNTRY varchar(2),
						BANDWIDTH long,
						UPTIME int, 
						IP_ADDR varchar(15),
						HOSTNAME varchar(35),
						OR_PORT long,
						DIR_PORT long,
						PLATFORM varchar(25),
						FIRST_SEEN varchar(10),
						AS_NAME varchar(25),
						AS_NUMBER long,
						C_BANDWIDTH long,
						OR_ADDR varchar(35)
						);''')
			print "DB created...!!!"
			#execute the dbupdate function to update the database(dump info in DB)
			print "Updating DB...!!!"
			self.update_DB()
		
		else:
			print "DB Connection error...!!!"
		
	def connect_db(self):
		conn = sqlite3.connect('data.db')
		if conn:
			return conn
		else:
			return -1
	
	def get_file(self):
		url = urllib.urlopen('https://torstatus.blutmagie.de/query_export.php/Tor_query_EXPORT.csv')
		dump = url.readlines()
		dump.pop(0)
		return dump
		
		

def main():
	startTime = datetime.now()
	app = readFile()
	print datetime.now() - startTime


if __name__ == '__main__':
	
	main()