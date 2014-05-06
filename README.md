## hastyBuild
---

Build script for Hasty Popcorn.
**This build was only tested on a Unix platform, so it might need some modification to work on Windows.**

###Dependencies

python 2, npm, nodejs, grunt and bower

1. Python 2 : https://www.python.org/download/
2. nodejs and npm : http://nodejs.org/
3. grunt and bower : ```$ npm install -g grunt-cli bower```

You also need a clone of Popcorn offical repo on your local disk :
```$ git clone https://github.com/popcorn-official/popcorn-app```

###Usage

One simple command :
```$ ./hasty_build.py path/of/popcorn/repo```

This generate builds for each platforms + compressed versions in the build folder

###Issues

You may have to set the correct permissions on `hasty_build.py` to get it to run :
```$ sudo chmod 755 hasty_build.py```
