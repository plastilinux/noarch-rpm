all: clean
	mkdir -p _build && \
	tar czf runscripts.tgz runscripts.d && \
	rpmbuild --define="%_topdir `pwd`/_build"  --define "%_sourcedir `pwd`" -bb runme.spec && \
	cp _build/RPMS/noarch/*rpm .

clean:
	rm -rf _build runscripts.tgz *rpm
