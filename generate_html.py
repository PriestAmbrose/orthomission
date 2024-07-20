import os

# Example data for the reading plan
reading_plan = {
    "01-01": "Matthew 1:1-17",
    "01-02": "Matthew 1:18-25",
    # Add more readings here
}

# Folder to store the HTML files
output_dir = "reading_plan_site"
os.makedirs(output_dir, exist_ok=True)

# Create the gospel reading plan page
gospel_html = "<html><head><title>Gospel Reading Plan</title></head><body>"
gospel_html += "<h1>Gospel Reading Plan for the Year</h1>"
gospel_html += "<table border='1'>"
gospel_html += "<tr><th>Date</th><th>Reading</th></tr>"

for date, reading in reading_plan.items():
    gospel_html += f"<tr><td>{date}</td><td>{reading}</td></tr>"

gospel_html += "</table></body></html>"

# Write the page to a file
with open(os.path.join(output_dir, "gospel.html"), "w", encoding='utf-8') as file:
    file.write(gospel_html)

# Create the index page
index_html = "<html><head><title>Orthomission</title></head><body>"
index_html += "<h1>Welcome to Orthomission</h1>"
index_html += "<p><a href='/gospel'>Gospel Reading Plan</a></p>"
index_html += "</body></html>"

# Write the index page to a file
with open(os.path.join(output_dir, "index.html"), "w", encoding='utf-8') as file:
    file.write(index_html)

print("HTML files have been successfully generated in the folder", output_dir)
