if [ -z $UPSTREAM_REPO ]

then

  echo "Cloning main Repository"

  git clone https://github.com/Aadhi000/ved.git /ved

else

  echo "Cloning Custom Repo from $UPSTREAM_REPO "

  git clone $UPSTREAM_REPO /ved

fi

cd /ved

pip3 install -U -r requirements.txt

echo "Starting ᗩᒍᗩ᙭....🔥"

python3 bot.py
