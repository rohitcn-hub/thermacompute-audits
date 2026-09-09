from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime

# Create PDF
doc = SimpleDocTemplate("audit_report.pdf", pagesize=letter)
story = []

# Title
story.append(Paragraph("ThermaCompute Audit Report", None))
story.append(Spacer(1, 20))

# Date
story.append(Paragraph(f"Generated: {datetime.now()}", None))
story.append(Spacer(1, 20))

# Dummy analysis
story.append(Paragraph("Thermal Waste Analysis:", None))
story.append(Spacer(1, 12))

# Dummy table
data = [
    ['Metric', 'Value'],
    ['GPU-Hours Lost', '142'],
    ['$ Wasted', '$12,450'],
    ['Throttling Events', '37'],
]
table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))
story.append(table)

# Build PDF
doc.build(story)
print("PDF generated: audit_report.pdf")
