test:
	nosetests --with-coverage --cover-package=buzio --cover-min-percentage=80
	pydocstyle --match-dir=buzio
	pycodestyle buzio/

break:
	nosetests -v --nocapture --ipdb

coverage:
	coverage report -m