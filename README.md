This is a template I use to start new Django projects.

It supports up to Django 1.6 and does not use CBV. It has a basic app included with a single view and a base bootstrap HTML template.

Sets you up with:
* South 0.8.4
* Bootstrap (css & js) 3.1.1
* jQuery 1.1.0

To customize this with the name of your project, you could run commands such as these: (projectname & appname are yours to choose)
```bash
git clone git@github.com:jboutros/djangotemplate.git projectname
cd projectname
rm -rf .git
find . -name "*\.py" -o -name "*\.default" -type f | xargs sed -i '' 's/djangotemplate/projectname/g'
mv firstapp appname
git init .
```
