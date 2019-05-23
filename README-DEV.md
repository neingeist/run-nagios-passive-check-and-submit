Update RPM
==========
* Bump version in `setup.py`
* Bump version in .spec
  * Do not forget to check Release!
* `git commit`
* `git tag -a -m '0.x.y' 0.x.y`
* `git push`
* `git push --tags`
* `python setup.py sdist`, `mv dist/*.tar.gz ~/rpmbuild/SOURCES`
* `rpmbuild -ba .spec`
