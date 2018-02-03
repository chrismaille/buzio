test:
	nosetests -v --with-coverage --cover-package=buzio --cover-min-percentage=70
	# pydocstyle --match-dir=buzio
	pycodestyle buzio/

break:
	nosetests -v --nocapture --ipdb

coverage:
	coverage report -m