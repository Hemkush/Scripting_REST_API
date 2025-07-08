import csv
from string import Template
# file = open('TestTimingData.csv', 'r')
# reader = csv.reader(file)
# for row in reader:
#     print(row)
timing_data = []
with open('TestTimingData.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        timing_data.append(row)

# print(timing_data)

column_chart_data = [["Test Name", "Diff from Avg"]]
table_data = [["Test Name", "Run Time (s)"]]

for row in timing_data[1:]:
    if not row[1] or not row[2]:
        print(f"Skipping row due to missing data: {row}")
        continue
    try:
        current_run_time = float(row[1])
        average_run_time = float(row[2])
    except ValueError:
        print(f"Skipping row due to ValueError: {row}")
        
    difference = current_run_time - average_run_time  # Assuming row[1] is the current run time
    column_chart_data.append([row[0], difference])  # Assuming row[1] is the current run time and row[2] is the average run time
    table_data.append([row[0], row[1]])

html_template = Template("""
<!DOCTYPE html>
<html>
<head> 
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
                         function drawChart() {
                         var data = google.visualization.arrayToDataTable([
       $labels
       $data,
      ],
      false); // 'false' means that the first row contains labels, not data.
        var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(data, options);
                         }
</script> 
</head>
<body><div id="chart_div" style="width:800; height:600"></div></body>
</html>
""")

chart_data_str = ''
for row in column_chart_data[1:]:
    chart_data_str += "%s,\n"%row
    
print(chart_data_str)
print(column_chart_data[0])
completed_html = html_template.substitute(labels=column_chart_data[0], data=chart_data_str)


with open('chart_data.html', 'w') as chart_file:
    chart_file.write(completed_html)

# print(column_chart_data)
# print(table_data)