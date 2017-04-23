#!/usr/bin/env python3

import json
from datetime import datetime

STATUS_KEY = {
	'Intro Ask': 1,
	'To Contact': 1,
	'Cold Email/InMail': 2,
	'Email/InMail':2,
	'Cold Email/ InMail': 2,
	'Email/ InMail':2,
	'Emailed Re: Session': 2,
	'Call HR': 3,
	'Call Data Teams': 3,
	'Reping': 4,
	'Scheduling': 5,
	'Scheduled': 5,
	'Visit': 5,
	'Demo': 6,
	'Direct Intro': 6,
	'Offer': 7,
	'Hire': 8,
	'Maybe Later': 9,
	'Not Hiring': 9
}


class Account:

	def __init__(self, company):
		self.company = company
		self.status = []
		self.event = {}

	def add_status(self, timeStamp, sessionStatus):
		self.status.append([timeStamp,sessionStatus])

	def add_line(self, line):
		if self.company == line[1]:
			self.add_status(line[0], line[6])

	def mapStatus(self, status):
		if status in STATUS_KEY:
			return STATUS_KEY[status]
		else:
			print(self.company+" Warning:"+status+" doesn't exist in status list.")

	def getEvents(self):
		"""
		Find status change (events) of an acccount and how many days it takes; only counts two consecutive status
		e.g. 'Call Data Teams' to 'Scheduling' takes 6 days
		"""
		while self.status:
			if self.status[0][1] == self.status[-1][1]: # if no event changes, report 0
				self.event['eventNum'] = 0
				self.event['events'] = {self.status[-1][1]: len(self.status)} # {eventNum: 0; 
																				#events:{
																				#	to contact: 29}
																				#	}
				return self.event
			else:
				events = [[0, self.status[0][1]]]	# report 0 for initial status from input time period
				for i in range(len(self.status)-1):
					if self.status[i][1] != self.status[i+1][1]:
						events.append([i+1, self.status[i+1][1]])  #[[0, to contact], [3, emailed re:sesssion], [18, call]]
				self.event['eventNum'] = len(events)-1
				self.event['events']={events[0][1] : events[0][0]}
 				for i in range(1,len(events)):	# count days between two status (event change)
					self.event['events'][events[i][1]] = events[i][0]-events[i-1][0]
				return self.event

	def getStatusMatrix(self):
		# statusMatrix = []
		# for ele in self.status:
		# 	statusMatrix.append(self.mapStatus(ele[1]))
		statusMatrix = [(x[0],self.mapStatus(x[1])) for x in self.status]
		return statusMatrix


		
				 








