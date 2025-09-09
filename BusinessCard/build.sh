echo "BUILD START"
python3 -m pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput --clear
mkdir -p staticfiles/media/
cp -r media/* staticfiles/media/
echo "BUILD END"
