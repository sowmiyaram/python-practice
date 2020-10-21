test: 1 2 3 4
.PHONY: test

%:
	python3 src/patterns.py $*
