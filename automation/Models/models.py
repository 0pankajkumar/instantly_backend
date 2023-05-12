class Email:
	def __init__(self):
		self.email_id = None
		self.smtp_address = None
		self.smtp_port = None
		self.imap_address = None
		self.imap_port = None


class Message:
	def __init__(self):
		self.body = None
		self.subject = None


class SenderEmail(Email):
	def __init__(self):
		pass