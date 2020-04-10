pip3 uninstall ndtreepy
git rm -r dist
git rm -r build
git rm -r ndtreepy.egg-info
rm -r dist
rm -r build
rm -r ndtreepy.egg-info
git add .
git commit -m "remove old build"

