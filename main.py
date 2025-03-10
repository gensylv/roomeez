from fpdf import FPDF

class Bill:
    """
    Contains data about a bill, such as
    total amount and time period.
    Calculates shares of the bill owed by any number of roomies.
    """

    def __init__(self, total, period):
        self.total = total
        self.period = period

class Roomie:
    """
    Represents a roommate responsible for a share of the bill.
    """

    def __init__(self, name, days_home):
        self.name = name
        self.days_home = days_home

    def pays(self, bill, roomies):
        total_days = sum(r.days_home for r in roomies)
        return (self.days_home / total_days) * bill.total

    def __repr__(self):
        return f"{self.name}, {self.days_home} days at home"

class PdfReport:
    """
    Generates a pdf report conveying data about all roomies and
    their shares of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, roomies, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Courier', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Roomies' Shared Bill", border=1, align='C', ln=1)

        # Insert period label and value
        pdf.cell(w=150, h=40, txt="Period:", border=1)
        pdf.cell(w=0, h=40, txt=bill.period, border=1, align='C', ln=1)

        # Insert names and amounts due for each roomie
        for r in roomies:
            pdf.cell(w=150, h=40, txt=r.name, border=1)
            pdf.cell(w=0, h=40, txt=f"${r.pays(bill, roomies):.2f}", border=1, ln=1)

        pdf.output(self.filename)


bill = Bill(120, "February 2025")
rm1 = Roomie("Rogue", 25)
rm2 = Roomie("Vill", 15)
rm3 = Roomie("Sly", 30)

bill_shares_report = PdfReport("roomies_bill.pdf")
bill_shares_report.generate([rm1, rm2, rm3], bill)

