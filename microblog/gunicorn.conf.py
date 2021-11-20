bind = 'unix:/var/run/microblog/microblog.sock'
workers = 2
worker_connections = 1000
max_requests = 1000
 
debug = False
daemon = True
pidfile = '/var/run/gunicorn/pid'
 
user = 'nginx'
group = 'nginx'
 
errorlog = '/var/log/gunicorn/microblog-error.log'
accesslog = '/var/log/gunicorn/microblog-access.log'
 
loglevel = 'info'
proc_name = 'microblog'
