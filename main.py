from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_pages = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_pages)

for indeed_job in indeed_jobs:
  if(indeed_job['company'] is None):
    print(indeed_job)