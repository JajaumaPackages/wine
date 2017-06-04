default: sources
	rpmbuild -ba *.spec -D "_sourcedir ${CURDIR}"
sources:
	spectool --get-files *.spec
