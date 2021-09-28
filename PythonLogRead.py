from urllib.request import urlretrieve

#pull log file from url and store it locally
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_LOG_FILE = 'log_local.log'
log_file, headers = urlretrieve(URL, LOCAL_LOG_FILE)

count1 = 0
count2 = 0

#loop through the file to see how many requests were made in the last 6 months
for line in open(log_file):
  if "May/1995" in line:
    count1 += 1
  elif "Jun/1995" in line:
    count1 += 1
  elif "Jul/1995" in line:
    count1 += 1
  elif "Aug/1995" in line:
    count1 += 1
  elif "Sep/1995" in line:
    count1 += 1
  elif "Oct/1995" in line:
    count1 += 1    
print("Total requests made in the last 6 months:",count1)


#loop through the file to count lines of data
for line in open(log_file):
  if "1994" in line or "1995" in line:
    count2 += 1 
print("Total requests made in the time period represented by the log:",count2)
