.PHONY: bench test report

build:
	virtualenv .
	bin/easy_install funkload

test:
	bin/fl-run-test loadtest.py

bench:
	bin/fl-run-bench loadtest.py GeoIPTest.test_geoip

report:
	bin/fl-build-report --html -o html simple-bench.xml
