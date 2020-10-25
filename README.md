✅ run.py <— — > job_scraper.py = scraped_data.json

✅ convert.py = converted_data.json

First run run.py, then convert.py to output scraper jobs to correct Sorting Jobs format. TO DO: Run skill_scanner to atuo-fill skill list in converted_data.json

TO DO
---

skill_scanner.py
- open job link
- grab description
- use nltk to parse out everything but verbs and nouns
- run parsed data against skills data set
- add detected skills to skills attribute in respective jobs data
