from omni-email import send_email
from Models.models import Message, SenderEmail
from dummy_data import sender_emails_dict


class Automation:
	def __init__(self):
		self.pool_of_emails = list()
		self.pool_of_receipient_emails = list()
		self.populate_pool_of_emails()
		self.populate_pool_of_receipient_emails()


	def populate_pool_of_emails(self):
		sender_email = SenderEmail()


		for email_dict in sender_emails_dict:

			sender_email.email_id = email_dict.email_id
			sender_email.smtp_address = email_dict.smtp_address
			sender_email.smtp_port = email_dict.smtp_port




		self.pool_of_emails = sender_email

	def populate_pool_of_receipient_emails(self):
		pass

	def send_email(self, email):
		send_email(email)

	def mark_email_sent(self):
		pass

	def bot(self):
		"""
		Process:
		1. Assumption: Pools of emails are pre populated
		2. Loop over the pool of emails
			a. Pick a random email from recipient pool, call this B
			b. Send email to this email address B
			c. Mark in the DB and SenderEmail object about the sending count & other sending statistics
		"""

		for email in pool_of_emails:
			self.send_email(email)
			self.mark_email_sent(email)



		

