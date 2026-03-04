class Report:
    def __init__(self, message, reporter_name=None):
        if not message or message.strip() == "":
            raise ValueError("Report message cannot be empty")

        self.message = message
        self.reporter_name = reporter_name
        self.status = "Pending"

    def update_status(self, new_status):
        if new_status not in ["Pending", "Reviewed", "Resolved"]:
            raise ValueError("Invalid status")

        self.status = new_status