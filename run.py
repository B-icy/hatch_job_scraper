import job_scraper
from job_scraper import find_jobs_from

desired_characs = ["titles", "companies", "links", "date_listed", "summary"]

find_jobs_from("Indeed", "Software Engineer", "san francisco", desired_characs)
