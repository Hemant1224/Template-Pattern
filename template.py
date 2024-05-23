# Consider a software application where you need to generate reports in different formats, such as PDF and HTML. 
# The process to generate a report involves common steps like fetching data and formatting the report, but the final rendering step is different for each format. 
# Using the Template Design Pattern, you can define the skeleton of the report generation process in a base class and allow subclasses to customize the rendering step.



from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    def generate_report(self):
        self.fetch_data()
        self.format_report()
        self.render_report()

    def fetch_data(self):
        print("Fetching data...")

    def format_report(self):
        print("Formatting report...")

    @abstractmethod
    def render_report(self):
        pass

class PDFReportGenerator(ReportGenerator):
    def render_report(self):
        print("Rendering report as PDF")

class HTMLReportGenerator(ReportGenerator):
    def render_report(self):
        print("Rendering report as HTML")

# Client code
pdf_report = PDFReportGenerator()
pdf_report.generate_report()

html_report = HTMLReportGenerator()
html_report.generate_report()
