import job_scraper
from job_scraper import find_jobs_from

desired_characs = ["titles", "companies", "links"]

find_jobs_from("Indeed", "product manager", "san francisco", desired_characs)