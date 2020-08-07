dev-setup:
	python pip install -e ".[test]"

tests:
	py.test tests --cov=webob_graphql -vv