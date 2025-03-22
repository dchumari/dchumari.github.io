import pandas as pd 
from jobspy import scrape_jobs


def scraper():
	jobs = scrape_jobs(
	    site_name='linkedin',
	    search_term='Data Scientist',
	    is_remote=True,
	    results_wanted=20,
	    easy_apply=False,
	    linkedin_fetch_description=True,
	)

	jobs = jobs.sort_values('date_posted', ascending=False)

	return jobs

if __name__ == "__main__":
	# print(scraper())
	for row in scraper().iterrows():
		print(row)
		print('***'*10)
