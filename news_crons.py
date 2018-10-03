from crontab import CronTab
#APP_COMMAND = "workon inshorts;python /Users/bavanari.m/Desktop/Inshorts-API/app.py"
NEWS_COMMAND = "/Users/bavanari.m/.virtualenvs/inshorts/bin/python /Users/bavanari.m/Desktop/Inshorts-API/news_display.py"

cron = CronTab()
# app_job = cron.new(command = APP_COMMAND)
# app_job.day.every(1)

news_job = cron.new(command = NEWS_COMMAND)
news_job.hour.every(6)

for item in cron:  
    print item
cron.write(user = "bavanari.m")